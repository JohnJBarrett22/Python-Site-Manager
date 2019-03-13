import os
import smtplib
import requests

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECEIVER = 'moo'

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