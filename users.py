from sets import Set

class Users(object):
  def __init__(self):
    self.users_map = {}

  def update_user(self, user_email, user_topics):
    if user_email not in self.users_map:
      user_topics_set = Set()
      for user_topic in user_topics:
        user_topics_set.add(user_topic)
      self.users_map[user_email] = user_topics_set
      print ("A new user " + user_email + " is created with topics " + str(self.users_map[user_email]))
    else:
      user_topics_set = self.users_map[user_email]
      for user_topic in user_topics:
        user_topics_set.add(user_topic)
      self.users_map[user_email] = user_topics_set
      print ("User " + user_email + " has updated his topics to " + str(self.users_map[user_email]))

#users = Users()
#users.update_user('ankurch@gmail.com', ['science', 'economy'])
#users.update_user('ankurch@gmail.com', ['tech'])
