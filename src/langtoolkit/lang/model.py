import spacy
from langtoolkit.config import get_config

_MODEL_DICT = {'sm': {'en': 'en_core_web_sm',
                 'es': 'es_core_news_sm'},
          'md': {'en': 'en_core_web_md',
                 'es': 'es_core_news_md'},
          'lg': {'en': 'en_core_web_lg',
                 'es': 'es_core_news_lg'},
          }


_MODEL = None
def load_model():
    global _MODEL

    if _MODEL is None:
        model_name  = get_model_name()
        _MODEL = {lang:spacy.load(model_name[lang])  for lang in model_name}
    return _MODEL

def get_model_name():
    return  _MODEL_DICT[get_config()['spacy']['model_size']]
            