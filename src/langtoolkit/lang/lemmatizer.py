import spacy
from langtoolkit.lang.model import load_model

MODELS = {'sm': {'en': 'en_core_web_sm',
                 'es': 'es_core_news_sm'},
          'md': {'en': 'en_core_web_md',
                 'es': 'es_core_news_md'},
          'lg': {'en': 'en_core_web_lg',
                 'es': 'es_core_news_lg'},
          }


class Lemmatizer:
    def __init__(self):
        self.lemm = load_model()
        
    def apply(self, lang, text):
        if not lang in self.lemm:
            return text
        doc = self.lemm[lang](text)
        return " ".join([token.lemma_ for token in doc])
