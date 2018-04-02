# Topic suggestor

A light-weight python module, that generate suggested topics for a given topic from the sources 
like google, bing.

Have plans to add suggestions based on NLP .

## Install

```bash

pip install topic-suggestor
```


## Usage

```python

from topic_suggestor import get_suggestions

result = get_suggestions(topic="molecule", sources=['google', 'bing', 'thesaurus'])
print(result)
#{'topic': 'molecule', 'suggested_topics': {'google': ['molecules', 'molecule definition', 'molecule air bar', 'molecules meaning', 'molecules meaning in hindi', 'molecules of emotion', 'molecule man', 'molecule examples', 'molecule definition chemistry', 'molecules journal'], 'bing': ['molecules', 'molecules youtube', 'molecules india', 'molecule facebook', 'molecule search', 'molecules pdf', 'molecules in hindi', 'molecules meaning'], 'thesaurus': ['fragment', 'particle', 'jot', 'speck', 'minim', 'mote', 'modicum', 'bit', 'mite', 'iota', 'unit', 'ray', 'ounce']}}


```
