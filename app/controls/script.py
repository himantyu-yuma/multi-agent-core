from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

from controls.llm import chatGpt
from domain.memory.mongoDB import MongoChatMessageHistory
from settings.get_template import get_template


def create_script(topic: str):
    """
    指定されたトピックについて、三姉妹の台本を作る
    """
    template = get_template("CreateScript")

    mongo_uri = "mongodb://root:root@mongo:27017/messages?authSource=admin"
    history = MongoChatMessageHistory(
        session_id=topic, connection_string=mongo_uri, collection_name="script"
    )
    memory = ConversationBufferMemory(
        chat_memory=history, memory_key="chat_history"
    )

    prompt = PromptTemplate(
        template=template,
        input_variables=["topic"],
    )

    chain = LLMChain(llm=chatGpt, prompt=prompt, memory=memory)
    result = chain.run({"topic": topic})
    history.client.close()

    return result


if __name__ == "__main__":
    sample = create_script("三姉妹は学食をこれから食べる予定であり、チキンタツタ丼がおすすめであることについて話している")
    print(sample)
