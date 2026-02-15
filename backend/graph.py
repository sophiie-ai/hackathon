import os
import base64
import requests
from typing import TypedDict, Literal, List
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

# --- STATE DEFINITION ---
class AgentState(TypedDict):
    phone_number: str
    messages: List[str]
    name: str | None
    issue_summary: str | None
    next_step: Literal["onboarding", "triage", "scheduling", "end"]

# --- THE BRAINS ---
text_llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))
vision_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# --- HELPERS ---
def download_twilio_image(url: str):
    """Downloads an image from Twilio using Basic Auth and returns Base64."""
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    
    response = requests.get(url, auth=HTTPBasicAuth(account_sid, auth_token))
    if response.status_code == 200:
        return base64.b64encode(response.content).decode("utf-8")
    else:
        print(f"❌ Image Download Error: {response.status_code}")
        return None

# --- NODES ---

def onboarding_node(state: AgentState):
    print("--- NODE: Onboarding ---")
    last_msg = state["messages"][-1]
    
    # Check if user sent a photo before telling us their name
    if "https://api.twilio.com" in last_msg:
        print("📸 Photo-first user detected. Jumping to Triage.")
        return {"next_step": "triage"}

    prompt = f"Extract name from: '{last_msg}'. Return ONLY the name. If no name, return 'NONE'."
    name_resp = text_llm.invoke(prompt).content.strip()
    
    if "NONE" not in name_resp.upper():
        return {
            "name": name_resp, 
            "next_step": "triage", 
            "messages": [f"Nice to meet you, {name_resp}! How can I help? You can describe the problem or send a photo."]
        }
    
    return {"next_step": "onboarding", "messages": ["Hi! I'm Sophiie. What's your name so I can help you out?"]}

def triage_node(state: AgentState):
    print("--- NODE: Triage (Hybrid) ---")
    last_msg = state["messages"][-1]
    
    if "https://api.twilio.com" in last_msg:
        print("--- Downloading and Analyzing Image ---")
        b64_image = download_twilio_image(last_msg)
        
        if not b64_image:
            return {"next_step": "end", "messages": ["I'm sorry, I couldn't access that photo. Could you try sending it again?"]}

        vision_prompt = "Identify the trade issue in this photo, estimate repair time in hours, and rate urgency 1-10."
        
        # Pass as Base64 data URI
        msg = HumanMessage(content=[
            {"type": "text", "text": vision_prompt},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{b64_image}"}
        ])
        
        analysis = vision_llm.invoke([msg]).content
        return {"issue_summary": analysis, "next_step": "scheduling", "messages": [f"Analysis: {analysis}"]}
    
    summary = text_llm.invoke(f"Summarize this issue: {last_msg}").content
    return {"issue_summary": summary, "next_step": "scheduling", "messages": [f"I've logged that: {summary}"]}

def scheduling_node(state: AgentState):
    print("--- NODE: Scheduling ---")
    return {"next_step": "end", "messages": ["Checking the tech's schedule... We can get someone there tomorrow at 9 AM. Does that work?"]}

# --- ROUTING ---
def route_logic(state: AgentState):
    if state["next_step"] == "onboarding":
        return END
    return state["next_step"]

workflow = StateGraph(AgentState)
workflow.add_node("onboarding", onboarding_node)
workflow.add_node("triage", triage_node)
workflow.add_node("scheduling", scheduling_node)

workflow.set_entry_point("onboarding")
workflow.add_conditional_edges("onboarding", route_logic, {"triage": "triage", "__end__": END})
workflow.add_edge("triage", "scheduling")
workflow.add_edge("scheduling", END)

app_graph = workflow.compile()