import spacy
from langtoolkit.config import get_config

MODELS = {'sm': {'en': 'en_core_web_sm',
                 'es': 'es_core_news_sm'},
          'md': {'en': 'en_core_web_md',
                 'es': 'es_core_news_md'},
          'lg': {'en': 'en_core_web_lg',
                 'es': 'es_core_news_lg'},
          }


class Lemmatizer:
    def __init__(self, model_size=None):
        self.model_size = model_size if model_size else get_config()['spacy']['model_size']
        self.lemm = {lang:spacy.load(MODELS[self.model_size][lang])  for lang in MODELS[self.model_size]}
        
    def apply(self, lang, text):
        if not lang in self.lemm:
            return text
        doc = self.lemm[lang](text)
        return " ".join([token.lemma_ for token in doc])
