from setuptools import setup

setup(
    name='topic-suggestor',
    version='0.0.4',
    packages=['topic_suggestor'],
    url='https://github.com/rrmerugu/topic-suggestor',
    license='MIT License',
    author='rrmerugu',
    author_email='rrmerugu@gmail.com',
    install_requires=['beautifulsoup4', 'lxml', 'requests'],
    description='A light-weight python module, that generate suggested topics for a given topic from the sources like google, bing. '
)
