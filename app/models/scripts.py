import datetime

from pydantic import BaseModel


class CreateScriptRequest(BaseModel):
    topic: str
    instraction: str
    published_at: datetime.datetime

    class Config:
        schema_extra = {
            "example": {
                "topic": "学食",
                "instraction": "三姉妹は学食をこれから食べる予定であり、チキンタツタ丼がおすすめであることについて話している",
                "published_at": datetime.datetime(2023, 5, 19, 12, 0, 0),
            }
        }
class UpdateScriptRequest(BaseModel):
    published_at: datetime.datetime

    class Config:
        schema_extra = {
            "example": {
                "published_at": datetime.datetime(2023, 5, 19, 12, 0, 0),
            }
        }
