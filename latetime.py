import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN_JIYUN = os.getenv("TOKEN_JIYUN")
MODE = os.getenv("MODE")
LOCATION = os.getenv("LOCATION")
myTokens = [
  {
    "name": "박지윤",
    "code": TOKEN_JIYUN,
    "text": "2시간 늦출"
  }
]

now = time.localtime()
year = now.tm_year
month = now.tm_mon
date = now.tm_mday
day = now.tm_wday

def post_message(token, channel, text):
  response = requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text}
  )
  print(response, now)

def 출퇴근유동제():
  for data in myTokens: 
    channel = "test-jiyun" if MODE=='test' else "#request-출퇴근유동제"
    additional = "\n" + LOCATION
    post_message(
      data["code"], 
      channel, 
      "[" + data["name"] + "] " + time.strftime('%m월 %d일 ') + data["text"] + additional
    )

# test
# for data in myTokens: 
#   post_message(data["code"], "test-jiyun", "[" + data["name"] + "] " + time.strftime('%m월 %d일 ') + data["text"])

# run
# schedule.every().day.at("00:01").do(출퇴근유동제)
# while True:
#   schedule.run_pending()
#   time.sleep(1)

# 크론으로 돌릴거라면 그냥 실행하자
출퇴근유동제()