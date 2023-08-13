import datetime

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pymongo.errors import DuplicateKeyError

from controls import agent_response, script, user_response
from models.agent_response import CreateAgentResponseRequest
from models.scripts import CreateScriptRequest, UpdateScriptRequest
from models.user_response import CreateUserResponseRequest

app = FastAPI()

origins = [
    "http://localhost:3030",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return {"data": script.filter_scripts(published_date)}


@app.get("/scripts/{script_id}")
async def get_script(script_id: str):
    """
    台本取得用エンドポイント
    """
    return script.get_script(script_id)

@app.put("/scripts/{script_id}")
async def put_scripts(script_id: str, req: UpdateScriptRequest):
    return script.update_script(script_id, {"published_at": req.published_at})

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
    return {"data": user_response.filter_user_responses(script_id)}


@app.get("/responses/user/{response_id}")
async def get_user_response(response_id: str):
    """
    idからユーザーの返答を取得する用エンドポイント
    """
    return user_response.get_user_response(response_id)


@app.post("/responses/agent")
async def post_agent_response(req: CreateAgentResponseRequest):
    """
    ユーザーの返答を受けた会話の続き生成用エンドポイント
    """
    try:
        res = agent_response.create_agent_response_by_user_response(
            req.user_response_id
        )
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400,
            detail="Duplicated Key: user_response_id",
        )
    return res


@app.get("/responses/agent")
async def get_agent_responses(script_id: str | None = None):
    """
    台本に紐づいているエージェントの返答取得用エンドポイント
    """
    return {"data": agent_response.filter_agent_responses(script_id)}


@app.get("/responses/agent/{response_id}")
async def get_agent_response(response_id: str):
    """
    idからエージェントの返答を取得する用エンドポイント
    """
    return agent_response.get_agent_response(response_id)
