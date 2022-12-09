import requests
import os
import time
from dotenv import load_dotenv
load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")
LOCATION = os.getenv("LOCATION")

def post_message(token, channel, text):
  response = requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text}
  )
  print(LOCATION + ": ", response, time.localtime())

def 봇테스트():
  post_message(TOKEN_BOT, "test-jiyun", "하이")

# test
봇테스트()