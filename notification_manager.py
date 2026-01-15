import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv


load_dotenv()

class Notification_Manager:
    def __init__(self, objet="", mess=""):
        self.username = os.environ['MAIL_FUNCTION_USERNAME']
        self.password = os.environ['MAIL_FUNCTION_PASSWORD']
        self.my_email = os.environ['MAIL_FONCTION_MYEMAIL']
        self.objet = objet
        self.message = mess

    def send_email(self, objet, mess, to=os.environ['MAIL_FONCTION_MYEMAIL']):
        msg = MIMEMultipart()
        msg['From'] = os.environ['MAIL_FONCTION_MYEMAIL']
        msg['To'] = to
        msg['Subject'] = objet
        msg.attach(MIMEText(mess, 'plain'))

        with smtplib.SMTP('smtp.mail.me.com', 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(self.my_email, self.password)
            connection.send_message(msg)


