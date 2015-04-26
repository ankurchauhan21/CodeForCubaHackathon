import imaplib
import email

class Receiver(object):
  def __init__(self):
    self.IMAP_GMAIL_HOST = "imap.gmail.com"
    self.IMAP_GMAIL_PORT = 993
    self.login_username = "news.janela"
    self.login_password = "windowcuba"

  def read_emails(self):
    conn = imaplib.IMAP4_SSL(self.IMAP_GMAIL_HOST, self.IMAP_GMAIL_PORT)
    conn.login(self.login_username, self.login_password)
    conn.select()
    typ, data = conn.search(None, 'ALL')
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
        full_text = subject + " " + body
        print(user_email)
        print(full_text)
    finally:
      try:
        conn.close()
      except:
        pass
        conn.logout()

Receiver().read_emails()
