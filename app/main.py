import datetime

from fastapi import FastAPI

from controls import script
from models.scripts import CreateScriptRequest

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


@app.post("/script")
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
