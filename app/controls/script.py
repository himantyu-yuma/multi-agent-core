from langchain import PromptTemplate
from langchain.chains import LLMChain

from controls.llm import chatGpt
from settings.get_template import get_template


def create_script(topic: str):
    """
    指定されたトピックについて、三姉妹の台本を作る
    """
    template = get_template("CreateScript")

    prompt = PromptTemplate(
        template=template,
        input_variables=["topic"],
    )

    chain = LLMChain(llm=chatGpt, prompt=prompt)
    result = chain.run({"topic": topic})

    return result


if __name__ == "__main__":
    sample = create_script("三姉妹は学食をこれから食べる予定であり、チキンタツタ丼がおすすめであることについて話している")
    print(sample)
