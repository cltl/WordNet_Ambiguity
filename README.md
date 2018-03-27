# WordNet Ambiguity

This repository provides a way to compute the WordNet ambiguity of a sequence of text.

The class **Ambiguity** in **ambiguity.py** makes it possible to compute this.

The script **ambiguity_browser.py** makes it possible to have a web interface.

**Requirements**

* Flask
* Spacy
* NLTK
* Tested with Python 3.6, but newer versions probably work just fine.
    
The Spacy model can installed by:
* pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-1.2.1/en_core_web_md-1.2.1.tar.gz
* python -m spacy link en_core_web_md en_default

