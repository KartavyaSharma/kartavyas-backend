"""
SendGrid mail handler, sends emails to kartavyas and senders
"""

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def html_client_gen(target_name, target_email):
    """
    Generates HTML for mailing to client.

    :target_name:       (string) First name of sender
    :target_email:      (string) Email of sender

    :return: HTML template as an fstring to be used with SendGrid's API service
    """
    content = f'
        <html>
            <head>    
                <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
            </head>            
            <div class="app font-sans min-w-screen min-h-screen bg-grey-lighter py-8 px-4">
              <div class="mail__wrapper max-w-md mx-auto">
                <div class="mail__content bg-white p-8 shadow-md">
                  <div class="content__header h-64 flex flex-col items-center justify-center text-center tracking-wide leading-normal bg-black -mx-8 -mt-8">
                      <h1 class="text-red text-5xl">Thank you</h1>
                      <p class="text-white text-2xl">For reaching out!</p>
                  </div>
                  <div class="content__body py-8 border-b">
                    <p>
                      Hey {target_name}!<br><br>
                      Thanks for contacting me. This is just a confirmation email. Your form submission on <a href="https://kartavyas.com">kartavyas.com</a> has been recieved!<br><br>
                      Keep an eye out for a reply in your <a href="mailto:{target_email}">{target_email}</a> inbox. I will get back to you as soon as possible.
                    </p>
                    <p class="mt-5">
                      Cheers!<br>
                      Kartavya Sharma
                    </p>
                  </div>
                  <div class="content__footer mt-8 text-center text-grey-darker">
                    <h3 class="text-base sm:text-lg mb-4">In the meantime, consider spreading the word!</h3>
                    <p><a href="https://kartavyas.com">www.kartavyas.com</a></p>
                  </div>
                </div>
                <div class="mail__meta text-center text-sm text-grey-darker mt-8">
                  <div class="meta__social flex justify-center my-4">
                    <a href="#" class="flex items-center justify-center mr-4 bg-black text-white rounded-full w-8 h-8 no-underline"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" class="flex items-center justify-center mr-4 bg-black text-white rounded-full w-8 h-8 no-underline"><i class="fab fa-instagram"></i></a>
                    <a href="#" class="flex items-center justify-center bg-black text-white rounded-full w-8 h-8 no-underline"><i class="fab fa-twitter"></i></a>
                  </div>
                  <div class="meta__help">
                    <p class="leading-loose">
                      Questions or concerns? <a href="#" class="text-grey-darkest">kartavya@kartavyas.com</a>
                      <br>
                      Not interested in future communication? <a href="#" class="text-grey-darkest">Unsubscribe</a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
        </html>
    '
    return content


def html_home_gen(fname, lname, email, message):
    """
    Generates HTML for mailing to private blog owner creator email ID.

    :fname:     (string) First name of sender
    :lname:     (string) Last name of sender
    :email:     (string) Email of sender
    :message:   (string) Message from sender

    :return: HTML template as an fstring to be used with SendGrid's API service
    """
    content = f'

    '
    return content


def home_mailer(first_name, last_name, email, message):
    message = Mail(
        from_email=os.environ.get('SENDER'),
        to_emails=os.environ.get('TARGET'),
        subject='Sending with Twilio SendGrid is Fun',
        html_content=''
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return True 
    except Exception as e:
        return {'False': e.message}


def client_mailer(client_name, client_email):
    message = Mail(
        from_email=os.environ.get('SENDER'),
        to_emails=f'{client_email}'
        subject='Successful form submission on kartavyas.com!'
        html_content=html_client_gen(client_name, client_email)
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return True
    except Exception as e:
        return {'False': e.message}


