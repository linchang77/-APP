import requests
import json
import time
import os

class WenxinYiyanChatBot:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.access_token = self.get_access_token()
        self.api_url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token={self.access_token}"
        self.conversation_history = []

    def get_access_token(self):
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret_key
        }
        response = requests.post(url, params=params)
        response.raise_for_status()
        return response.json().get("access_token")

    def get_response(self, message):
        # 提示回答尽可能简短
        prompt = "请尽量简短地回答: " + message
        self.conversation_history.append({"role": "user", "content": prompt})
        payload = json.dumps({
            "messages": self.conversation_history
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.api_url, headers=headers, data=payload)
        response.raise_for_status()
        res = response.json()
        bot_message = res.get('result', '抱歉，我不明白你的意思。')
        self.conversation_history.append({"role": "assistant", "content": bot_message})
        return bot_message

    def read_questions_and_write_responses(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            questions = infile.readlines()
            for question in questions:
                response = self.get_response(question.strip())
                print(f"问题: {question.strip()}\n回答: {response}\n")
                outfile.write(response)

def get_file_modification_time(filepath):
    return os.path.getmtime(filepath)


    
