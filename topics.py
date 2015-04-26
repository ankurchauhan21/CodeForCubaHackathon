class Topics(object):
  def __init__(self):
    self.TOPICS = ['sports', 'technology', 'lifestyle']

  def parse_topics(self, text):
    text = text.lower()
    topics = []
    for topic in self.TOPICS:
      if topic in text:
        topics.append(topic)
    return topics

#Topics().parse_topics("Technology is not in ScIEnce")
