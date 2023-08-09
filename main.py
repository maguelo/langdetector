from langtoolkit.lang.detector import load_data, LanguageDetector

if __name__ == "__main__":
    # print(ROOT_PATH)

    print(load_data().keys())
    print(load_data()['es'][:10])
    print(load_data()['en'][:10])
    detector = LanguageDetector()
    print(detector.detect("Hola mundo cruel"))
    print(detector.metrics)
    print(detector.threshold)
    print(detector.metrics_last)

