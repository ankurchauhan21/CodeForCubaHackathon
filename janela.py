import smtplib

class Users:
  def __init__(self):
    self.users_list = ['ankurchauhan21@gmail.com',
                       'albaleal@gmail.com',
                       'rodriguez.gretchen@gmail.com',
                       'coelholds@gmail.com',
                       'hkunamneni@hotmail.com',
                       'amy168@gmail.com']

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
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(self.username, self.password)
    server.sendmail(self.fromaddr, user, self.msg)
    server.quit()

def main():
  send_stories = SendStories()
  send_stories.send_stories_to_users()

if __name__ == "__main__":
  main()
