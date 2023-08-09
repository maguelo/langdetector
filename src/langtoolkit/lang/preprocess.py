import re
from unidecode import unidecode


def remove_accents(text):
    return unidecode(text)

def lowercase(text):
    return text.lower()

def remove_special(text):
    return re.sub('[^A-Za-z0-9.]+', ' ', text)

def remove_spaces(text):
    return text.strip()

def split_multiple_words(text):
    candidate = text.split(" ")
    if len(candidate) == 1:
        return candidate[0]
    return ""

def remove_small_word(text, threshold=3):
    if len(text) > threshold:
        return text
    return ""

class Pipeline:
    def __init__(self):
        self.pipeline = []

    def register(self, method):
        self.pipeline.append(method)

    def apply(self, text):
        for method in self.pipeline:
            text = method(text)
        return text
