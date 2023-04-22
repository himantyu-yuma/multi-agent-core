"""
llmのモデルを返す
"""
from langchain.chat_models import ChatOpenAI

from settings.api_setting import API_KEY

chatGpt = ChatOpenAI(
    openai_api_key=API_KEY, model_name="gpt-3.5-turbo", temperature=0.7
)
