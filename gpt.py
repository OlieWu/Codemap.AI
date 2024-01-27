import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
api_key = os.getenv('GPT_KEY')
print(api_key)