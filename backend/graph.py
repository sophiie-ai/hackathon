import os
from typing import TypedDict, Literal, List
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Define the State
class AgentState(TypedDict):
    phone_number: str
    messages: List[str]
    name: str | None
    next_step: Literal["onboarding", "triage", "scheduling", "end"]

# Initialize Gemini
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# --- NODES ---

def onboarding_node(state: AgentState):
    print(f"--- NODE: Onboarding ---")
    last_msg = state["messages"][-1]
    
    # AI logic to extract name
    prompt = f"Extract only the person's name from this message: '{last_msg}'. If no name is mentioned, reply 'NONE'."
    response = llm.invoke(prompt).content.strip()
    
    if "NONE" not in response.upper() and len(response) < 50:
        return {
            "name": response,
            "next_step": "triage",
            "messages": [f"Nice to meet you, {response}! What can I help you with? You can describe the issue or send a photo."]
        }
    
    return {
        "next_step": "onboarding", 
        "messages": ["Hi! I'm Sophiie. To get started, what is your name?"]
    }

def triage_node(state: AgentState):
    print("--- NODE: Triage ---")
    # Here is where you'll eventually add the Vision tool call
    return {"next_step": "scheduling", "messages": ["I've noted that down. Checking our availability..."]}

def scheduling_node(state: AgentState):
    print("--- NODE: Scheduling ---")
    return {"next_step": "end", "messages": ["We have a slot tomorrow at 8:00 AM. Does that work?"]}

# --- ROUTER LOGIC (The Fix) ---

def route_after_onboarding(state: AgentState):
    # If the AI is still asking for a name, we MUST stop and wait for user
    if state["next_step"] == "onboarding":
        return END
    return "triage"

# --- GRAPH CONSTRUCTION ---

workflow = StateGraph(AgentState)

workflow.add_node("onboarding", onboarding_node)
workflow.add_node("triage", triage_node)
workflow.add_node("scheduling", scheduling_node)

workflow.set_entry_point("onboarding")

# Apply the router
workflow.add_conditional_edges(
    "onboarding",
    route_after_onboarding,
    {
        "triage": "triage",
        "end": END  # This maps END to the actual graph stop
    }
)

workflow.add_edge("triage", "scheduling")
workflow.add_edge("scheduling", END)

app_graph = workflow.compile()