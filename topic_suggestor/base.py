from .bing import get_bing_suggestions
from .google import get_google_suggestions
from .thesaurus import Word


def get_suggestions(topic=None, sources=[], lang=None, country=None):
    result = {}
    if sources is []:
        sources = ['bing', 'google']
    result['topic'] = topic
    result['suggested_topics'] = {}
    if "google" in sources:
        result['suggested_topics']['google'] = get_google_suggestions(topic=topic, lang=lang)
    if "bing" in sources:
        result['suggested_topics']['bing'] = get_bing_suggestions(topic=topic, lang=lang)

    if "thesaurus" in sources:
        thesaurus = Word(topic)
        result['suggested_topics']['thesaurus'] = thesaurus.synonyms()
    return result
