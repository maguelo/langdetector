import argparse
import pickle
from langtoolkit.lang.preprocess import *
from langtoolkit.lang.loader import load_word_from_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script that generates Spanish dictionary resource")
    parser.add_argument(
        "input", help="input file in txt format, one word per line")
    parser.add_argument("output", help="output file in pickle format")
    args = parser.parse_args()

    pipeline = Pipeline()
    pipeline.register(lowercase)
    pipeline.register(remove_accents)
    pipeline.register(remove_special)
    pipeline.register(remove_spaces)
    pipeline.register(split_multiple_words)
    pipeline.register(remove_small_word)

    with open(args.input, mode='r', encoding='utf-8') as file:
        spanish_words = load_word_from_file(file.readlines(), pipeline)
    print(spanish_words[:10])

    with open(args.output, 'wb') as handle:
        pickle.dump(spanish_words, handle, protocol=pickle.HIGHEST_PROTOCOL)
