"""
This is the mail_controller module, it supports all mail operations
for kartavyas
"""

from flask import make_response, abort

def send_mail(body):
    """
    Mailer function that uses SendGrids handlers to send mail.

    :body:      A dictionary containing form data
    :return:    Create success/failed response for server
    """
    
    
