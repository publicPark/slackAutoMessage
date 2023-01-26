import os
from pies import slackkk
from google_cal import calcalcal
import time
import random

from dotenv import load_dotenv
load_dotenv()
TOKEN_USER = os.getenv("TOKEN_USER")
MODE = os.getenv("MODE")
LOCATION = os.getenv("LOCATION")
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")
NAME = os.getenv("NAME")

from datetime import date
today = date.today()

#
def 출근시간_슬랙():
  res = None
  try:   
    res = calcalcal.get_event()
  except Exception as e:
    print("error: ", e)

  text = "2시간 늦출"

  print("calendar get event result: ", res)

  if res != None:
    if res == '휴일':
      return
    elif res:
      text = res
  
  channel = "test-jiyun" if MODE=='test' else "#"+TARGET_CHANNEL
  additional = "\n" + LOCATION
  slackkk.post_message(
    TOKEN_USER, 
    channel, 
    "[" + NAME + "] " + str(today.month) + "월 " + str(today.day) + "일 " + text + additional
  )


# 크론으로 돌릴거라면 그냥 실행하자
time.sleep(random.uniform(0, 1000))
출근시간_슬랙();