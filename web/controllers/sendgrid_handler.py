"""
SendGrid mail handler, sends emails to kartavyas and senders
"""

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def home_mailer():
    message = Mail(
        from_email=os.environ.get('SENDER'),
        to_emails=os.environ.get('TARGET'),
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with python.</strong>'
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def client_mailer():
    pass
