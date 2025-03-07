from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Message(BaseModel):
    user: str
    content: str

messages: List[Message] = []

@app.post("/send")
async def send_message(message: Message):
    messages.append(message)
    return {"status": "Message received"}

@app.get("/messages")
async def get_messages():
    return messages