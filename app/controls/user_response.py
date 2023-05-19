from langchain import LLMChain, PromptTemplate

from controls.llm import chatGpt
from settings.get_template import get_template


def create_user_response(sentence: str):
    """
    入力文から推測されるユーザーの返答を返す
    """
    template = get_template("CreateResponse")

    prompt = PromptTemplate(template=template, input_variables=["sentence"])

    chain = LLMChain(llm=chatGpt, prompt=prompt)
    result = chain.run({"sentence": sentence})

    return result


if __name__ == "__main__":
    s = """
サイ：こんにちは、エマ、ノイ。今日は学食で何を食べようかしら。
エマ：私はチキンタツタ丼がおいしいって聞いたことがあるわ。
ノイ：そうだよね、私も食べたことあるけど、おすすめだよ。
    """
    res = create_user_response(s)
    print(res)
