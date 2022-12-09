# slackAutoMessage   
## install packages   
pip install requests python-dotenv   
   
## test   
python3 test.py   
   
## env   
vim .env   
   
## cron   
crontab -e   
0 3 * * 1-5 /usr/bin/python3 /home/ubuntu/slackAutoMessage/latetime.py   
   
## log   
0 3 * * 1-5 /usr/bin/python3 /home/ubuntu/slackAutoMessage/latetime.py > /home/ubuntu/slackAutoMessage/test.log 2>&1