from pydantic import BaseModel


class CreateUserResponseRequest(BaseModel):
    script_id: str
    break_point: int

    class Config:
        schema_extra = {
            "example": {
                "script_id": "64661c7cab6e66270e943696",
                "break_point": 3,
            }
        }


class GetUserResponsesRequest(BaseModel):
    script_id: str
