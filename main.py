from sender import Sender
from receiver import Receiver
from time import sleep
from users import Users

def main():
  users = Users()
  receiver = Receiver()
  sender = Sender()
  while True:
    receiver.read_emails(users)
    for (user_email, user_topics) in users.users_map.items():
      sender.send_news(user_email, list(user_topics))
    print ('Sleeping')
    sleep(20)
    print ('Waking up')

if __name__ == "__main__":
  main()
