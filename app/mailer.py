import os
import smtplib
from email.mime.text import MIMEText
from typing import List


def send_email(msg, recipients: List[str]):
    sender = 'noreply@festive-lights.com'

    msg['Subject'] = '504 Error'
    msg['From'] = sender
    msg['To'] = recipients[0]

    with smtplib.SMTP(os.getenv('SMTP_HOST'), os.getenv('SMTP_PORT')) as server:
        server.starttls()
        server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))
        server.sendmail(sender, recipients, msg.as_string())