"""
This is the mail_controller module, it supports all mail operations
for kartavyas
"""

from flask import make_response, abort

def send_mail(body):
    print(type(body))
    
