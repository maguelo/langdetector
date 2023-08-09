
import os
import pickle

from langtoolkit.config import get_config,get_resources_path
from langtoolkit.lang.preprocess import Pipeline
from langtoolkit.lang.lemmatizer import Lemmatizer

DICTIONARY = None


def load_data(config=None):

    config = config if config else get_config()

    global DICTIONARY
    if DICTIONARY is None:
        DICTIONARY = {}
        for lang in config['lang']:
            lang_file = os.path.join(
                get_resources_path(), config['lang'][lang])
            with open(lang_file, 'rb') as handle:
                DICTIONARY[lang] = pickle.load(handle)

    return DICTIONARY


class LanguageDetector:
    DEFAULT = "UNK"
    def __init__(self, dictionary=None, preprocess=None, lemmatizer=None, threshold=None):
        self.dictionary=dictionary if dictionary else load_data()
        self.preprocess = preprocess if preprocess else Pipeline()
        self.lemmatizer = lemmatizer if lemmatizer else Lemmatizer()
        self.threshold = threshold if threshold else get_config()['detector']['threshold']

        self.metrics_last = {} 
        self.metrics = {lang:0 for lang in self.dictionary}
        self.metrics.update({'total':0,self.DEFAULT:0})
        
    def _update_metrics(self, key):
        self.metrics[key]+=1
        self.metrics['total']+=1
        
    def detect(self, text):
        self.metrics_last = {lang:0 for lang in self.dictionary}
        total=0

        for token in text.split(" "):
            token = self.preprocess.apply(token)
            if token:
                for lang in self.dictionary:
                    if token in self.dictionary[lang]:
                        self.metrics_last[lang]+=1
                    else:
                        lemma_en = self.lemmatizer.apply(lang,token)
                        if lemma_en in self.dictionary[lang]:
                            self.metrics_last[lang]+=1
                total+=1
                        
    
        if total==0:
            self._update_metrics(self.DEFAULT)
            return self.DEFAULT
        
        for lang in self.metrics_last:
            self.metrics_last[lang]/=total

        result = list(self.metrics_last.items())
        result.sort(key=lambda x:x[1],reverse=True)

        if result[0][1]>self.threshold:
            self._update_metrics(result[0][0])
            return result[0][0]

        self._update_metrics(self.DEFAULT)
        return 'UNK'
