import datetime

from pydantic import BaseModel


class CreateScriptRequest(BaseModel):
    topic: str
    instraction: str
    published_at: datetime.datetime
