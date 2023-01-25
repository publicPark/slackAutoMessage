# slackAutoMessage   
슬랙을 매일매일 보내야하는데 귀찮아서 만들었다! 오늘이 며칠인지도 모르겠고! 귀찮아!   
   
## install packages   
pip install requests python-dotenv   
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   
## test   
python3 test.py   
   
## env   
vim .env   
   
## credentials.json, token.json   
cat > token.json   
   
## cron   
crontab -e   
   
## cron test   
30 14 * * * /usr/bin/python3 /home/ubuntu/slackAutoMessage/test.py   
타임존이 이상할껄? 타임존은 알아서 설정하기.
   
   
## cron setting - run!
0 3 * * 1-5 /usr/bin/python3 /home/ubuntu/slackAutoMessage/latetime.py   
   
## log   
0 3 * * 1-5 /usr/bin/python3 /home/ubuntu/slackAutoMessage/latetime.py > /home/ubuntu/slackAutoMessage/test.log 2>&1
   