from sets import Set
from topics import Topics

class User(object):
  def __init__(self, email, topics):
    self.modified = True
    self.email = email
    self.topics_set = Set()
    self._add_topics(topics)

  def update_topics(self, topics):
    self._add_topics(topics)

  def print_self(self):
    return (self.email + ' ' + str(self.topics_set) + ' ' + str(self.modified))

  def _add_topics(self, topics):
    self.modified = True
    if not topics:
      topics = Topics().TOPICS
    for topic in topics:
      self.topics_set.add(topic)

class Users(object):
  def __init__(self):
    self.users_map = {}

  def update_user(self, user_email, user_topics):
    if user_email not in self.users_map:
      user = User(user_email, user_topics)
      self.users_map[user_email] = user
      print ("User created " + user.print_self())
    else:
      user = self.users_map[user_email]
      user.update_topics(user_topics)
      self.users_map[user_email] = user
      print ("User modified " + user.print_self())

#users = Users()
#users.update_user('ankurch@gmail.com', ['science', 'economy'])
#users.update_user('ankurch@gmail.com', ['sports'])
#users.update_user('none1@gmail.com', None)
#users.update_user('none2@gmail.com', [])
