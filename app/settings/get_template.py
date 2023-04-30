import pathlib

base_dir = pathlib.Path(__file__).parent / "templates"


def get_template(name: str) -> str:
    # テンプレートが無かったらエラー出す
    if name in base_dir.glob("*"):
        raise Exception("no template exception")
    temp = ""
    with open(base_dir / f"{name}.txt", mode="r", encoding="utf-8") as f:
        temp = f.read()
    return temp


# FIXME: デバッグ用なので消す
if __name__ == "__main__":
    print(get_template("NOI"))
