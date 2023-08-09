# langtoolkit
Tools for working with natural language


## Installation
```
pip install git+https://github.com/maguelo/langtoolkit.git
```

### Spacy dictionaries

#### Small size: sm
```
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm
```

#### Medium size: md

```
python -m spacy download en_core_web_md
python -m spacy download es_core_news_md
```

#### Large size: lg
```
python -m spacy download en_core_web_lg
python -m spacy download es_core_news_lg
```
Remember to modify the config file to specify the model size, default: large


## Example
```
from langtoolkit.lang.detector import LanguageDetector
from langtoolkit.tools.preprocess import *

pipeline = Pipeline()
pipeline.register(lowercase)
pipeline.register(remove_accents)
pipeline.register(remove_special)
pipeline.register(remove_spaces)
pipeline.register(split_multiple_words)
pipeline.register(remove_small_word)

detector = LanguageDetector(preprocess=pipeline)
detector.detect("Hello world")
```