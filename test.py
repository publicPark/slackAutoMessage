import requests
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")

def post_message(token, channel, text):
  response = requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text}
  )
  print(response)

def 봇테스트():
  post_message(TOKEN_BOT, "test-jiyun", "하이")

# test
봇테스트()