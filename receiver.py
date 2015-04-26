import imaplib
import email

from email.header import decode_header, make_header

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])



def parse_subject(encoded_subject):
        dh = decode_header(encoded_subject)
        default_charset = 'ASCII'
        return ''.join([ unicode(t[0], t[1] or default_charset) for t in dh ])

def start_receiver():
  conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
  conn.login("news.janela", "windowcuba")
  conn.select()
  typ, data = conn.search(None, 'ALL')
  try:
    for uid in data[0].split():
      response, results = conn.fetch(uid, '(BODY.PEEK[] FLAGS X-GM-THRID X-GM-MSGID X-GM-LABELS)')
      raw_message = results[0]
      raw_email = raw_message[1]
      message = email.message_from_string(raw_email)
      if message.get_content_maintype() == "multipart":
        for content in message.walk():
          if content.get_content_type() == "text/plain":
            body = content.get_payload(decode=True)
          elif content.get_content_type() == "text/html":
            html = content.get_payload(decode=True)
      elif self.message.get_content_maintype() == "text":
        body = message.get_payload()
      subject = parse_subject(message['subject'])
      print(subject)
      print(body)
  finally:
    try:
      conn.close()
    except:
      pass
      conn.logout()

def main():
  start_receiver()

if __name__ == "__main__":
  main()
