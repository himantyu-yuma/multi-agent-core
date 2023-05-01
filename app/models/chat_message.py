from pydantic import BaseModel


class ChatMessage(BaseModel):
    content: str


class ChatMessageWithSpeaker(BaseModel):
    speaker: str
    content: str
