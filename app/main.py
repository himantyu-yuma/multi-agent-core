from fastapi import FastAPI

from controls.chat_chain import chat_with_charactor
from controls.classify import classify
from models.chat_message import ChatMessage, ChatMessageWithSpeaker

# NOTE: 型定義は外部から呼び出す
from models.speaker import Speaker

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
async def chat(message: ChatMessageWithSpeaker):
    """
    チャット用エンドポイント
    """
    address = classify(sentence=message.content, speaker=message.speaker)
    # ユーザー向けのメッセージは無視
    if address == "User":
        return
    result = chat_with_charactor(address, message.content)
    return {"speaker": address, "content": result}


@app.post("/chat/{address}")
async def read_item(address: Speaker, message: ChatMessage):
    """
    特定のスピーカー向けエンドポイント
    """

    result = chat_with_charactor(address.value, message.content)
    return result
