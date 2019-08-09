import requests as rq
from bs4 import BeautifulSoup as bS
import smtplib as sm
import time

URL = 'https://store.steampowered.com/app/648800/Raft/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = rq.get(URL, headers=headers)

    soup = bS(page.content, 'html.parser')

    price = soup.find(class_ = 'discount_final_price').get_text()

    converted_price = float(price[1:])

    print(converted_price)
    if(converted_price > 10.00):
        send_mail()
    
    print('done')


def send_mail():
    server = sm.SMTP('smtp.gmail.com',587)
    #server.ehlo()
    server.starttls()
   # server.ehlo()
    
    server.login('allenchenschool@gmail.com','diuuuladkwqldwfo')

    subject = "check price drop!"
    body = "check https://store.steampowered.com/app/648800/Raft/"
    from_mail = 'allenchenschool@gmail.com'
    to = '942972518@tmomail.net'
    msg = ("From: %s\r\n" % from_mail + "To: %s\r\n" % to + "Subject: %s\r\n" % subject + "\r\n" + body)
    
    server.sendmail(
        from_mail,
        to,
        msg
    )



    server.quit()

#while True:
check_price()
    #time.sleep(60)

print('done')