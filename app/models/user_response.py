from pydantic import BaseModel


class CreateUserResponseRequest(BaseModel):
    script_id: str
    break_point: int


class GetUserResponsesRequest(BaseModel):
    script_id: str
