import requests


def get_google_suggestions(topic=None, lang=None):
    url = "http://suggestqueries.google.com/complete/search?q={}&client=firefox&hl={}".format(
        topic,
        lang
    )
    res = requests.get(url)
    suggested_topics = []
    try:
        suggested_topics = res.json()[1]
    except Exception as e:
        print(e)

    return suggested_topics
