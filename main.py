from langtoolkit.lang.detector import load_data, LanguageDetector
from langtoolkit.tools.preprocess import *
if __name__ == "__main__":
    # print(ROOT_PATH)

    print(load_data().keys())
    print(load_data()['es'][:10])
    print(load_data()['en'][:10])

    pipeline = Pipeline()
    pipeline.register(lowercase)
    pipeline.register(remove_accents)
    pipeline.register(remove_special)
    pipeline.register(remove_spaces)
    pipeline.register(split_multiple_words)
    pipeline.register(remove_small_word)

    detector = LanguageDetector(preprocess=pipeline)
    print(detector.detect("Hola mundo cruel"))
    print(detector.metrics)
    print(detector.threshold)
    print(detector.metrics_last)

