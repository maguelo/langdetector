import argparse
import pickle
from langtoolkit.tools.preprocess import *
from langtoolkit.lang.loader import load_word_from_file
import nltk
nltk.download('words')

from nltk.corpus import words

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script that generates English dictionary resource")
    parser.add_argument("output", help="output file in pickle format")
    args = parser.parse_args()

    pipeline = Pipeline()
    pipeline.register(lowercase)
    pipeline.register(remove_accents)
    pipeline.register(remove_special)
    pipeline.register(remove_spaces)
    pipeline.register(split_multiple_words)
    pipeline.register(remove_small_word)

   
    english_words = load_word_from_file(words.words(), pipeline)
    print(english_words[:10])

    with open(args.output, 'wb') as handle:
        pickle.dump(english_words, handle, protocol=pickle.HIGHEST_PROTOCOL)
