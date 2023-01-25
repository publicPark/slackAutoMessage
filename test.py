import os
from pies import slackkk
from dotenv import load_dotenv
load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")

def 봇테스트():
  slackkk.post_message(TOKEN_BOT, "test-jiyun", "하이")

# test
봇테스트()