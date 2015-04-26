class Topics(object):
  def __init__(self):
    self.TOPICS = ['sports', 'technology', 'science']

  def parse_topics(self, text):
    text = text.lower()
    topics = []
    for topic in self.TOPICS:
      if topic in text:
        topics.append(topic)
    print (topics)

#Topics().parse_topics("Technology is not in ScIEnce")
