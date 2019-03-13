import os
import smtplib
import requests
from linode_api4 import LinodeClient

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')
RECEIVER = 'moo'

client = LinodeClient(LINODE_TOKEN)

for linode in client.linode.instances():
    print(f'{linode.label}: {linode.id}')

r = requests.get('https://johnjbarrett.me', timeout = 5)

if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = '~~~WEBSITE IS DOWN!~~~'
        body = 'Make sure the server is restarted and is back up!'
        msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, RECEIVER, msg)