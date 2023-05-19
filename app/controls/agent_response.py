from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from controls.llm import chatGpt
from settings.get_template import get_template


def create_agent_response(
    instruction: str, agent_sentence: str, user_sentence: str
):
    """
    ユーザーからの返答を受けたエージェントの会話の続きを返す
    """
    system_template = get_template("CreateScript").format(topic=instruction)

    system_message_prompt = SystemMessagePromptTemplate(
        prompt=PromptTemplate(template=system_template, input_variables=[])
    )

    human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="ユーザー：{input}", input_variables=["input"]
        )
    )

    chat_propmpt_template = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    memory = ConversationBufferMemory()
    memory.chat_memory.add_ai_message(agent_sentence)
    memory.chat_memory.add_user_message(user_sentence)

    chain = LLMChain(llm=chatGpt, prompt=chat_propmpt_template, memory=memory)
    result = chain.predict(input=user_s)

    return result


if __name__ == "__main__":
    instruction = """
三姉妹は学食をこれから食べる予定であり、チキンタツタ丼がおすすめであることについて話している
    """
    agent_s = """
サイ：こんにちは、エマ、ノイ。今日は学食で何を食べようかしら。
エマ：私はチキンタツタ丼がおいしいって聞いたことがあるわ。
ノイ：そうだよね、私も食べたことあるけど、おすすめだよ。
    """
    user_s = """
それなら私もチキンタツタ丼を食べてみようかな。
    """
    res = create_agent_response(instruction, agent_s, user_s)
    print(res)
