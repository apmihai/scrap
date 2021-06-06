import requests
from bs4 import BeautifulSoup as bs
import smtplib
import csv
import json
from menu import menu
from decouple import config

# SEND EMAIL WITH ABOVE/BELOW PRICES FOR EMAG PRODUCTS

#-------------------Parse url
def get_data(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    title = soup.find(class_="page-title").get_text()
    title = title.strip()
    price = soup.find(class_="product-new-price").get_text()
    converted_price = float(price.strip()[0:5])*1000
    return title, converted_price

#-------------------Check price
def check_price(tinta, nr_mail, title, converted_price, url):
    if nr_mail == 1:                            # multiple mails
        if converted_price <= int(tinta):
            subject = f'Price below {tinta}!'
            body = f'Price for {title} is now {int(converted_price)} lei and target is {int(tinta)}. Check the link:\n\t{url}'
        else:
            subject = f'Price above {tinta}!'
            body =f'Price for {title} is {int(converted_price)} lei and target is {int(tinta)}. Still above...'
        send_mail(subject, body)
    if nr_mail == 2:                              # one mail
        if converted_price <= int(tinta):
            body = f'Price for {title} is now {int(converted_price)} lei and target is {int(tinta)}. Check the link:\n\t{url}\n\n'
        else:
            body = f'Price for {title} is {int(converted_price)} lei and target is {int(tinta)}. Still above...\n\n'
    return body

#-------------------Send mail
def send_mail(s, b):
    file_conf = open('config.json',)
    data_conf = json.load(file_conf)
    server_smtp = data_conf['smtpServer']
    server_port = data_conf['port']
    from_user = data_conf['fromUser']
    to_user = data_conf['toUser']
    server = smtplib.SMTP(server_smtp, server_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    userID = config('userID',default='')
    password = config('password',default='')
    server.login(userID,password)
    msg = f'Subject: {s}\n\n{b}'
    server.sendmail(from_user, to_user, msg)
    server.quit()

#-------------------Main
def mainf(nr_mail):
    #-------------------Create lists
    urls =[]
    tintas = []
    with open('favorites.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            urls.append(row[0])
            tintas.append(row[1])
    #-------------------Call functions
    print('Processing...')
    body = ''
    for url, tinta in zip(urls, tintas):
        title, converted_price = get_data(url)
        body = body + check_price(tinta, nr_mail, title, converted_price, url)
    if nr_mail == 2:
        subject = 'info favorites'
        send_mail(subject, body)    
    print('Done!')
    exit()
 
 #-------------------Menu
choice = menu().upper()
while choice != 'Q':
    if choice == '1':
        nr_mail = 1         # multiple mails
        mainf(nr_mail)
    if choice == '2':
        nr_mail = 2         # one email
        mainf(nr_mail)
    else:
        choice = menu()
exit()
