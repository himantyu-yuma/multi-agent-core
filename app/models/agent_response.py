from pydantic import BaseModel


class CreateAgentResponseRequest(BaseModel):
    user_response_id: str

    class Config:
        schema_extra = {
            "example": {
                "user_response_id": "64671d8a2fee3f8bbf4a8aa6",
            }
        }


class GetAgentResponsesRequest(BaseModel):
    script_id: str
