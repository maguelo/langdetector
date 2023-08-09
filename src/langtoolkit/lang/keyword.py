import textacy

from langtoolkit.lang.model import get_model_name


class KeywordExtractor:
    def __init__(self, top_words=10):
        self.model_name = get_model_name()
        self.model = {lang: textacy.load_spacy_lang(
            self.model_name[lang]) for lang in self.model_name}
        self.top_words = top_words

    def extract(self, lang, text):
        if lang in self.model:
            doc = textacy.make_spacy_doc(text, lang=self.model[lang])
            return [kps.lower() for kps, weights in textacy.extract.keyterms.sgrank(doc, topn=self.top_words)]
        print(f"Language {lang} unknown")
        return []


if __name__ == "__main__":
    keyword_extractor = KeywordExtractor()
    print(keyword_extractor.extract(
        'en', 'Apple is using deep learning to train the most advanced model in Artificial Intelligence.'))
