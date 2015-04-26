from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from news import News

import smtplib

class Sender(object):
  def send_news(self, user_email, user_topics):
    subject = 'Welcome to Janela - window to the world!!!'
    body = 'Your morning digest from Code for Cuba Hackathon\n\n'
    body += self.news.get_news(user_topics)
    print ('Sending news to ' + user_email + " for topics " + str(user_topics))
    self._send_email(user_email, subject, body)

  def __init__(self):
    self.username = 'news.janela'
    self.password = 'windowcuba'
    self.fromaddr = 'news.janela@gmail.com'
    self.news = News()

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

#Sender().send_news('ankurchauhan21@gmail.com', ['science', 'sports'])
