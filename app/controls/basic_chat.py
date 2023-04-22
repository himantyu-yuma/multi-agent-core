"""
agentを使わない、ベーシックな対話エージェント
"""
from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict

from controls.llm import chatGpt
from domain.memory.mongoDB import MongoChatMessageHistory

# 一旦mongo memory のテスト
memory = MongoChatMessageHistory(
    session_id="mongo_test",
    connection_string="mongodb://root:root@mongo:27017/messages?authSource=admin",
    collection_name="messages",
)

user_input = "user"

res = "res test"

memory.add_user_message(user_input)
memory.add_ai_message(res)

print(memory.messages)

print("--------")


memory.client.close()
