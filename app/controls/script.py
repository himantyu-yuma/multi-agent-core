import datetime
import re

from bson import ObjectId
from langchain import PromptTemplate
from langchain.chains import LLMChain

from controls.llm import chatGpt
from repository.database.mongoDB import MongoDB
from settings.get_template import get_template


def create_script(
    topic: str, instruction: str, published_at: datetime.datetime
):
    """
    指定されたトピックについて、三姉妹の台本を作る
    Args:
        topic: str : トピック(DB保存用)
        instruction: str : 生成させる際の命令
    Returns:
        生成された台本のmongo上のID
    """
    template = get_template("CreateScript")

    prompt = PromptTemplate(
        template=template,
        input_variables=["topic"],
    )

    chain = LLMChain(llm=chatGpt, prompt=prompt)
    result = chain.run({"topic": instruction})

    lines = result.split("\n")
    scripts = []
    line_order = 0
    for line in lines:
        if line == "":
            continue
        (speaker, quote) = re.split("[:：]", re.sub(" 　", "", line))
        scripts.append(
            {"order": line_order, "speaker": speaker, "quote": quote}
        )
        line_order += 1

    data = {
        "topic": topic,
        "scripts": scripts,
        "published_at": published_at,
        "created_at": datetime.datetime.now(),
    }

    client = MongoDB(collection_name="scripts")
    scripts_id = client.insert_one(data).inserted_id
    client.close_connection()

    return str(scripts_id)
    return result


if __name__ == "__main__":
    sample = create_script("三姉妹は学食をこれから食べる予定であり、チキンタツタ丼がおすすめであることについて話している")
    print(sample)
