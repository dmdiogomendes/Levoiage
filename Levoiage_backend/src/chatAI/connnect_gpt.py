from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
# 
def run_ai(query):
    dotenv_path = os.path.join(os.path.dirname(__file__), '../..','.env')
    load_dotenv(dotenv_path)

    api_key = os.getenv("CHATGPT")

    chat_model = ChatOpenAI(openai_api_key=api_key)

    result = chat_model.invoke(query)

    return result

