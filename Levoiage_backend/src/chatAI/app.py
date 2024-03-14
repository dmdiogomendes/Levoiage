from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/ask": {"origins": "http://localhost:8000"}})

def create_chat_model(query):
    dotenv_path = os.path.join(os.path.dirname(__file__), '../..','.env')
    load_dotenv(dotenv_path)

    api_key = os.getenv("CHATGPT")

    chat_model = ChatOpenAI(openai_api_key=api_key)

    result = chat_model.invoke(query)

    return result

#chat_model = create_chat_model()

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({'error': 'Missing "query" parameter'}), 400
    
    result = create_chat_model(query)

    if hasattr(result, 'text'):
        result = 'result.text'
    else:
        result = str(result)

    if result.startswith('content='):
        result = result[len('content='):]

    result = result.strip("'")    

    return jsonify({'response': result})

# this works, attention
@app.route('/test', methods=['GET'])
def test():
    # data = request.get_json()
    # query = data.get('query')

    return jsonify({'response': 'TEST FROM THE API WORKS'})

if __name__ == '__main__':
    app.run(debug=True)