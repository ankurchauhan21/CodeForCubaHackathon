from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import smtplib

class Users:
  def __init__(self):
    self.users_list = ['ankurchauhan21@gmail.com',
                       #'albaleal@gmail.com',
                       #'rodriguez.gretchen@gmail.com',
                       #'coelholds@gmail.com',
                       #'hkunamneni@hotmail.com',
                       #'amy168@gmail.com'
                       ]

class SendStories:
  def send_stories_to_users(self):
    users = Users()
    for user in users.users_list:
      self._send_email(user)

  def __init__(self):
    self.username = 'news.janela'
    self.password = 'windowcuba'
    self.fromaddr = 'news.janela@gmail.com'
    self.msg = 'Welcome to Janela - window to the world!!!'

  def _send_email(self, user):
    msg = MIMEMultipart()
    msg['From'] = self.fromaddr
    msg['To'] = user
    msg['Subject'] = 'Welcome to Janela - window to the world!!!'
    body = "Your morning digest: Code for cuba hackathon happening"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(self.username, self.password)
    text = msg.as_string()
    server.sendmail(self.fromaddr, user, text)
    server.quit()

def main():
  send_stories = SendStories()
  send_stories.send_stories_to_users()

if __name__ == "__main__":
  main()
