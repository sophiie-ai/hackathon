import os
from fastapi import FastAPI, Form
from twilio.twiml.messaging_response import MessagingResponse
from graph import app_graph
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
thread_store = {}

@app.post("/webhook")
async def reply(Body: str = Form(None), From: str = Form(...), MediaUrl0: str = Form(None)):
    user_input = MediaUrl0 if MediaUrl0 else Body
    print(f"📩 Incoming from {From}: {user_input}")

    if From not in thread_store:
        thread_store[From] = {
            "phone_number": From, "messages": [], "name": None, 
            "issue_summary": None, "next_step": "onboarding"
        }
    
    thread_store[From]["messages"].append(user_input)
    
    # Process with Graph
    updated_state = app_graph.invoke(thread_store[From])
    thread_store[From] = updated_state
    
    # Get AI response and Print for Debugging
    ai_reply = updated_state["messages"][-1]
    print(f"🤖 AI Response: {ai_reply}")
    
    resp = MessagingResponse()
    resp.message(ai_reply)
    return str(resp)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)