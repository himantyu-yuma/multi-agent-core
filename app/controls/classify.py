import json

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from controls.llm import chatGpt
from settings.get_template import get_template


def classify(sentence: str, speaker: str):
    template = get_template("Classify")

    prompt = PromptTemplate(
        input_variables=["sentence", "speaker"], template=template
    )
    chain = LLMChain(llm=chatGpt, prompt=prompt)
    result = chain.run({"sentence": sentence, "speaker": speaker})
    print(result)
    address = json.loads(result)["address"]
    return address


if __name__ == "__main__":
    print(classify("自己紹介お願いします", "User"))
