import requests
import random
from bs4 import BeautifulSoup


def get_bing_suggestions(topic=None, lang=None):
    url = "https://www.bing.com/AS/Suggestions?mkt={}&qry={}&cvid={}".format(lang,
                                                                             topic,
                                                                             str(random.randint(123, 21323123))
                                                                             )
    res = requests.get(url)
    suggested_topics = []
    try:
        soup = BeautifulSoup(res.text, "xml")
        section = soup.find('ul', attrs={'class': 'sa_drw'})
        elements = section.findAll('li', {'class': 'sa_sg'})
        for element in elements:
            query = element['query']
            if (len(query) != 0) and query != topic:
                suggested_topics.append(query)
    except Exception as e:
        print(e)
    return suggested_topics
