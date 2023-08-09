# import os
import spacy

# os.system('python -m spacy download en_core_web_sm')

MODELS={'sm':{'en':'en_core_web_sm',
                  'es':'es_core_news_sm'},
            'md':{'en':'en_core_web_md',
                  'es':'es_core_news_md'},
            'lg':{'en':'en_core_web_lg',
                  'es':'es_core_news_lg'},
            }

class Lemmatizer:
    def __init__(self, model_size='sm'):
        # Cargar los modelos de spaCy para inglés y español

        self.lemm = {"en":spacy.load(MODELS[model_size]['en']),
                     "es":spacy.load(MODELS[model_size]['es'])}

    def apply(self, lang, text):
        if not lang in self.lemm:
            return text
        doc = self.lemm[lang](text)
        return " ".join([token.lemma_ for token in doc])
