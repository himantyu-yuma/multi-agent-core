from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

from controls.llm import chatGpt
from domain.memory.mongoDB import MongoChatMessageHistory
from models.speaker import Speaker
from settings.get_template import get_template


def chat_with_charactor(address: Speaker, sentence: str):
    """
    addressに指定したキャラクターにsentenceを入力として与え、
    出力を返り値としてもらうための関数
    """
    template = get_template(address)
    system_prompt = SystemMessagePromptTemplate.from_template(template)

    mongo_uri = "mongodb://root:root@mongo:27017/messages?authSource=admin"

    # FIXME: session_idとか固定じゃダメな気がする
    history = MongoChatMessageHistory(
        session_id="temp",
        connection_string=mongo_uri,
        collection_name="sample",
    )
    memory = ConversationBufferMemory(
        chat_memory=history, memory_key="chat_history"
    )
    # XXX: なぜ↓のワンステップが必要なのか理解してない
    prompt = ChatPromptTemplate.from_messages([system_prompt])

    chain = LLMChain(llm=chatGpt, prompt=prompt, memory=memory)
    result = chain.run(sentence)
    return result


if __name__ == "__main__":
    noi_sample = chat_with_charactor("NOI", "自己紹介をお願いします。")
    # sai_sample = chat_with_charactor("SAI", "自己紹介をお願いします。")
    # ema_sample = chat_with_charactor("EMA", "自己紹介をお願いします。")
    print(noi_sample)
    # print()
    # print(sai_sample)
    # print()
    # print(ema_sample)
    # noi_sample = chat_with_charactor(
    #     "NOI",
    #     "有線イヤホンと無線イヤホンのどちらを購入するかというテーマで雑談を行います。まずはノイから話のきっかけとなる文章を出力してください。サイお姉ちゃんもしくはエマお姉ちゃんに対しての発言であることが好ましいです。",
    # )
    # print(noi_sample)
