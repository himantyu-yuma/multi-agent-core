import os

from dotenv import load_dotenv

load_dotenv()

# API KEY を外に出す
API_KEY = os.getenv("API_KEY")
