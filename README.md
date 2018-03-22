# Topic suggestor

A light-weight python module, that generate suggested topics for a given topic from the sources 
like google, bing.

Have plans to add suggestions based on NLP .

```python

from topic_suggestor import get_suggestions

result = get_suggestions(topic="molecular modelling", sources=['google', 'bing'])
print (result)

#{'topic': 'molecular modelling', 'suggested_topics': {'google': [], 'bing': ['molecular modelling pdf', 'molecular modelling ppt', 'molecular modelling book', 'molecular modelling wikipedia', 'molecular modelling tools', 'molecular modelling slideshare', 'molecular modelling journal']}}


```
