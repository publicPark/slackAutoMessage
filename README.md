# slackAutoMessage   
슬랙을 매일매일 보내야하는데 귀찮아서 만들었다! 오늘이 며칠인지도 모르겠고! 귀찮아!   
   
## install packages   
pip install requests python-dotenv   
   
## test   
python3 test.py   
   
## env   
vim .env   
   
## cron   
crontab -e   

## cron test
0 14 * * * /usr/bin/python3 /home/ubuntu/slackAutoMessage/test.py

## cron setting
0 3 * * 1-5 /usr/bin/python3 /home/ubuntu/slackAutoMessage/latetime.py   
CRON_TZ=Asia/Seoul  
   
## log   
0 3 * * 1-5 /usr/bin/python3 /home/ubuntu/slackAutoMessage/latetime.py > /home/ubuntu/slackAutoMessage/test.log 2>&1