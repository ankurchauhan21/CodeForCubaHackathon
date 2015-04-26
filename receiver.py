import imaplib
import email

from users import Users
from topics import Topics

class Receiver(object):
  def __init__(self):
    self.IMAP_GMAIL_HOST = "imap.gmail.com"
    self.IMAP_GMAIL_PORT = 993
    self.login_username = "news.janela"
    self.login_password = "windowcuba"
    self.topics = Topics()

  def read_emails(self, users):
    conn = imaplib.IMAP4_SSL(self.IMAP_GMAIL_HOST, self.IMAP_GMAIL_PORT)
    conn.login(self.login_username, self.login_password)
    conn.select()
    typ, data = conn.search(None, 'UNSEEN')
    try:
      for uid in data[0].split():
        response, results = conn.fetch(uid, '(BODY.PEEK[] FLAGS X-GM-THRID X-GM-MSGID X-GM-LABELS)')
        raw_message = results[0]
        raw_email = raw_message[1]
        message = email.message_from_string(raw_email)
        fr = message['from']
        user_name, user_email = email.utils.parseaddr(fr)
        subject = message['subject']
        if message.get_content_maintype() == "multipart":
          for content in message.walk():
            if content.get_content_type() == "text/plain":
              body = content.get_payload(decode=True)
            elif content.get_content_type() == "text/html":
              html = content.get_payload(decode=True)
        elif self.message.get_content_maintype() == "text":
          body = message.get_payload()
        typ, response = conn.store(uid, '+FLAGS', r'(\Seen)')
        full_text = subject + " " + body
        user_topics = self.topics.parse_topics(full_text)
        users.update_user(user_email, user_topics)
    finally:
      try:
        conn.close()
      except:
        pass
        conn.logout()

#users = Users()
#Receiver().read_emails(users)
