import os
import smtplib
import requests

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

r = requests.get('https://johnjbarrett.me', timeout = 5)

if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        body = 'Make sure the server is restarted and is back up!'
        subject = '~~~WEBSITE IS DOWN!~~~'