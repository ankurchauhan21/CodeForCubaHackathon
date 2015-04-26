from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import smtplib

class Sender(object):
  def send_news(self, user):
    subject = 'Welcome to Janela - window to the world!!!'
    body = 'Your morning digest from Code for Cuba Hackathon'
    print ('Sending news to ' + user)
    self._send_email(user, subject, body)

  def __init__(self):
    self.username = 'news.janela'
    self.password = 'windowcuba'
    self.fromaddr = 'news.janela@gmail.com'

  def _send_email(self, user, subject, body):
    msg = MIMEMultipart()
    msg['From'] = self.fromaddr
    msg['To'] = user
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(self.username, self.password)
    text = msg.as_string()
    server.sendmail(self.fromaddr, user, text)
    server.quit()

#Sender().send_news('ankurchauhan21@gmail.com')
