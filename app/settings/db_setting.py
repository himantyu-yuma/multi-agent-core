from pymongo import MongoClient

# FIXME: 環境変数から取得したい
CONNECTION_STRING = "mongodb://root:root@mongo:27017/messages?authSource=admin"

client = MongoClient(CONNECTION_STRING)
db = client.get_default_database()
user_collection = db["user_responses"]

# script_idとbreak_pointの組み合わせに一意のインデックスを作成
user_collection.create_index(
    [("script_id", 1), ("break_point", 1)], unique=True
)

agent_collection = db["agent_responses"]
agent_collection.create_index([("user_response_id", 1)], unique=True)

client.close()
