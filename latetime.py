import requests
import schedule
import time
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN_JIYUN = os.getenv("TOKEN_JIYUN")
myTokens = [
  {
    "name": "박지윤",
    "code": TOKEN_JIYUN,
    "text": "2시간 늦출"
  }
]

now = time
year = now.localtime().tm_year
month = now.localtime().tm_mon
date = now.localtime().tm_mday

def post_message(token, channel, text):
  response = requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text}
  )
  print(response)

def 출퇴근유동제():
  for data in myTokens: 
    post_message(data["code"], "#request-출퇴근유동제", "[" + data["name"] + "] " + now.strftime('%m월 %d일') + data["text"])

# run
schedule.every().day.at("00:00").do(출퇴근유동제)
while True:
  schedule.run_pending()
  time.sleep(1)
