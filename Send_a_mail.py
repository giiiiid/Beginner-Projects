# Import modules/tools to do the work
from email.message import EmailMessage
from Send import password
import ssl
import smtplib

# Setting your receiver, sender, password form gmail, subject and body of the email
email_sender = 'gideonnobbs@gmail.com'
email_password = password
email_receiver = 'gideonfummey1@gmail.com'

email_subject = 'Cann Legend'
email_body = '''We will be having a class at 1pm'''


# Creating an instance to send the email
em = EmailMessage()
em['sender'] = email_sender
em['receiver'] = email_receiver
em['subject'] = email_subject
em.set_content(email_body)

# Create a context to easily detect the email
context = ssl.create_default_context()

#Transferring the email from the gmail server ~ ssl, stmp.lib
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    