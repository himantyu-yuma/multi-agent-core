from fastapi import FastAPI

from models.chat_message import ChatMessage

# NOTE: 型定義は外部から呼び出す
from models.speaker import Speacker

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


@app.post("/chat")
async def chat(message: ChatMessage):
    """
    チャット用エンドポイント
    """
    return message


@app.post("/chat/{speaker}")
async def read_item(speaker: Speacker):
    """
    特定のスピーカー向けエンドポイント
    """
    return {"speaker": speaker}
