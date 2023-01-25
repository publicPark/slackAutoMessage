import requests
from datetime import datetime

# 슬랙보내기
def post_message(token, channel, text):
  response = requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text}
  )

  print(response, datetime.now())
