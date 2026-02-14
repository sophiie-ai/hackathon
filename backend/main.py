import os
from fastapi import FastAPI, Form, Request
from twilio.twiml.messaging_response import MessagingResponse
from graph import app_graph
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# In-memory store to keep track of user conversations
thread_store = {}

@app.get("/")
async def health_check():
    return {"status": "alive", "service": "sophiie-dispatch-agent"}

@app.post("/webhook")
async def reply(
    Body: str = Form(None), 
    From: str = Form(...),
    MediaUrl0: str = Form(None) # This catches the WhatsApp Photo
):
    print(f"Incoming from {From}: {Body if Body else 'Photo Message'}")
    
    # 1. Initialize State for new users
    if From not in thread_store:
        thread_store[From] = {
            "phone_number": From,
            "messages": [],
            "name": None,
            "address": None,
            "next_step": "onboarding"
        }
    
    # 2. Determine Input: Use Photo URL if available, otherwise use Text
    # If a photo is sent, user_input becomes the URL for Gemini to analyze
    user_input = MediaUrl0 if MediaUrl0 else Body

    if not user_input:
        return ""

    # 3. Update the conversation history
    thread_store[From]["messages"].append(user_input)
    
    # 4. Run the Brain (LangGraph)
    try:
        # We pass the current user state into the graph
        result = app_graph.invoke(thread_store[From])
        
        # 5. Save the updated state (so the AI remembers the name/issue)
        thread_store[From] = result
        
        # 6. Get the AI's latest response from the message list
        ai_response = result["messages"][-1]
        
        # 7. Format the Twilio WhatsApp Response
        resp = MessagingResponse()
        resp.message(ai_response)
        return str(resp)

    except Exception as e:
        print(f"❌ Error: {e}")
        resp = MessagingResponse()
        resp.message("Sorry, I encountered an error. Please try again!")
        return str(resp)

if __name__ == "__main__":
    import uvicorn
    # Running on your preferred port
    uvicorn.run(app, host="0.0.0.0", port=8001)