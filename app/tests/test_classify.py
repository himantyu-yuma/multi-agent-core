from controls.chat_chain import chat_with_charactor
from controls.classify import classify


def test_classify_address():
    """
    対象を正しく認識できているかのテスト
    LLMが対象なので厳密なチェックはできないが、最低でも80パーセントくらいの確率で
    通って欲しい
    """
    speaker = "NOI"
    sentence = chat_with_charactor(address=speaker, sentence="自己紹介をお願いします。")
    address = classify(sentence=sentence, speaker=speaker)
    assert address == "User"
