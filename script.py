# @author samuel bailey 
#please read txt file before using

import requests #webpull
from bs4 import BeautifulSoup #webpull
import smtplib #email server lib
import time #for delay 

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #connects to server
    server.starttls() #secure connection 
    server.ehlo() #reconnect securly

    server.login('demo@apple.com', 'enterpasswordhere') #login with your email 
    #items sent in email
    subject = 'Price fell down!'
    body = 'Go buy now! https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?dchild=1&keywords=Sony+mark+3&qid=1606836724&sr=8-3'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'demo@apple.com',
        'recieving@apple.com',
        msg
    )
    #confirmation message to recieve in terminal
    print('email sent')
    server.quit() #quit server link

#function to check the price of amazon product
def check_price():
    #insert any link you want to check the price of here
    URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?dchild=1&keywords=Sony+mark+3&qid=1606836724&sr=8-3'

    #your web browser header goes here | simply google user agent in your browser to get this number
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}

    #recieving your page
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    #setting certain things to pull so you don't have to pull the entire website each time
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text() # price is a string so it still needs to be converted
    converted_price = float(price[0:7]) # only pulls the first 7 digits of the price

    if(converted_price < 1,700): #this sends email if it falls under this price
        send_email()

    #TESTING
    #print(converted_price)
    #print(title.strip())

#actual running of the program. it checks the price every day at whatever time this was ran
while(True): 
    check_price()
    time.sleep(86400)