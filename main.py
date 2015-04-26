from sender import Sender
from receiver import Receiver
from time import sleep
from users import Users
from users import Users

def main():
  users = Users()
  receiver = Receiver()
  sender = Sender()
  while True:
    receiver.read_emails(users)
    for user in users.users_map.values():
      if user.modified:
        sender.send_news(user.email, list(user.topics_set))
        user.modified = False
    print ('Sleeping')
    sleep(10)
    print ('Waking up')

if __name__ == "__main__":
  main()
