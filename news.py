from topics import Topics

class News(object):
  def get_news(self, topics):
    stories = ""
    for topic in topics:
      #stories += "In the World of " + topic.upper() + "\n\n"
      stories += self.news[topic] + "\n\n"
    return stories

  def __init__(self):
    self.news = {}
    self.TOPICS = Topics().TOPICS
    for topic in self.TOPICS:
      self.news[topic] = self._get_news(topic)

  def _get_news(self, topic):
    file_path = 'news/' + topic + '.txt'
    print ("Reading news from " + file_path)
    f = open(file_path, 'r')
    news = f.read()
    f.close()
    return news

  def print_news(self):
    for (topic, story) in self.news.items():
      print (topic + " news\n")
      print (story)
      
#news = News()
#print news.get_news(['science', 'sports'])
#print news.get_news(['sports'])
#print news.get_news(['technology', 'science'])
