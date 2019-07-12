import requests
from bs4 import BeautifulSoup
import  smtplib
import time

#URL of the website
URL= 'https://www.amazon.in/Apple-iPhone-XR-64GB-Black/dp/B07JWV47JW/ref=sr_1_2_sspa?crid=91G0KF9H7XPP&keywords=iphone+xs+max&qid=1562876366&s=gateway&sprefix=iphone%2Caps%2C363&sr=8-2-spons&psc=1'

#Collecting information from the website
headers= {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page= requests.get(URL, headers=headers)

    #Parsing the information
    soup= BeautifulSoup(page.content, 'html.parser')

    title= soup.find(id="title").get_text()
    price= soup.find(id="priceblock_ourprice").get_text()
    commas_removed= price[2:8].replace(',','')
    converted_price= float(commas_removed)

    #Information about the item
    print("The Item is: {}".format(title))
    print("The Price of the item is: {}".format(converted_price))


    if converted_price<60000:
        send_mail()

def send_mail():
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #Make sure 'GOOGLE less secure apps' is turned on
    #Enter the Mailid and password for the account which will send the mail
    server.login('saptarshi6969@gmail.com','Sukumar@68')
    
    subject= 'Price fell down'
    body= 'check the amazon link: https://www.amazon.in/Apple-iPhone-XR-64GB-Black/dp/B07JWV47JW/ref=sr_1_2_sspa?crid=91G0KF9H7XPP&keywords=iphone+xs+max&qid=1562876366&s=gateway&sprefix=iphone%2Caps%2C363&sr=8-2-spons&psc=1'
    msg= "subject:{}\n\n{}".format(subject,body)

    server.sendmail(
        #senders email
        'saptarshi6969@gmail.com',
        #recivers email
        'saptarshi0009@gmail.com',
        #the message
        msg
    )
    print("email has been sent")

    #Stopping the server
    server.quit()

#Setting scheduler to check everyday
while True:
    check_price()
    time.sleep(60*60*24)



