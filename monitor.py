import os
import smtplib
import requests
from linode_api4 import LinodeClient, Instance

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')
RECEIVER = 'moo'

# for linode in client.linode.instances():
#     print(f'{linode.label}: {linode.id}')

def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = '~~~WEBSITE IS DOWN!~~~'
        body = 'Make sure the server is restarted and is back up!'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, RECEIVER, msg)

def reboot_server():
    client = LinodeClient(LINODE_TOKEN)
    my_server = client.load(Instance, 111111) #Need to get true ID, 111111 is dummy data
    my_server.reboot()

try:
    r = requests.get('https://johnjbarrett.me', timeout = 5)

    if r.status_code != 200:
        notify_user()
        reboot_server()
except Exception as e:
    notify_user()
    reboot_server()