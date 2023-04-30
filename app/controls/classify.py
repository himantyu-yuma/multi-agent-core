from settings.get_template import get_template
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from controls.llm import chatGpt


def classify(sentence: str, speaker: str):
    template = get_template("Classify")

    prompt = PromptTemplate(
        input_variables=["sentence", "speaker"], template=template
    )
    chain = LLMChain(llm=chatGpt, prompt=prompt)
    result = chain.run({"sentence": sentence, "speaker": speaker})
    return result


if __name__ == "__main__":
    print(classify("こんにちは！サイお姉ちゃんは今日何をしていたの？", "NOI"))
