import datetime

from fastapi import FastAPI, HTTPException
from pymongo.errors import DuplicateKeyError

from controls import script, user_response
from models.scripts import CreateScriptRequest
from models.user_response import CreateUserResponseRequest

app = FastAPI()


@app.on_event("shutdown")
def shutdown_event():
    # FIXME: mongo client をcloseする処理
    pass


# TODO: api dir以下に移動する？
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
async def ping():
    """
    疎通確認用エンドポイント
    """
    return


@app.post("/scripts")
async def post_script(req: CreateScriptRequest):
    """
    台本作成用エンドポイント
    """
    return script.create_script(req.topic, req.instraction, req.published_at)


@app.get("/scripts")
async def get_scripts(published_date: datetime.date | None = None):
    return script.filter_scripts(published_date)


@app.get("/scripts/{script_id}")
async def get_script(script_id: str):
    """
    台本取得用エンドポイント
    """
    return script.get_script(script_id)


@app.post("/responses/user")
async def post_user_response(req: CreateUserResponseRequest):
    """
    台本に基づいたユーザー返答生成用エンドポイント
    """
    try:
        res = user_response.create_user_response_by_script(
            req.script_id, req.break_point
        )
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400,
            detail="Duplicated Combination: script_id, break_point",
        )
    return res


@app.get("/responses/user")
async def get_user_responses(script_id: str | None = None):
    """
    台本に紐づいている返答取得用エンドポイント
    """
    return user_response.filter_user_responses(script_id)


@app.get("/responses/user/{response_id}")
async def get_user_response(response_id: str | None = None):
    """
    台本に紐づいている返答取得用エンドポイント
    """
    return user_response.get_user_response(response_id)
