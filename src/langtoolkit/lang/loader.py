from tqdm import tqdm
from langtoolkit.lang.preprocess import Pipeline


def load_word_from_file(corpus: str, preprocess: Pipeline = None)->list:
    """
    Load a list of words from a file. Preprocess all words if preprocess method is provided
    Args:
        corpus (str): List of words
        preprocess (Pipeline, optional): Preprocess method. Defaults to None.

    Returns:
        list: list of strings
    """
    list_words = set()
    preprocess = preprocess if preprocess else Pipeline()
    
    for word in tqdm(corpus):
        candidate = preprocess.apply(word)
        if candidate:
            list_words.add(candidate)
    list_words = list(list_words)
    list_words.sort()
    return list_words

