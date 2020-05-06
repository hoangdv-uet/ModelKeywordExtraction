# Keyword Extraction by NER model combine with Keyword

### Requirement:
    * flar
    * pandas
    * numpy
    * bs4
    * re
    * string

### How to get entities:
```python
from KeyWordExtraction import *

text = 'Bill Gate'
model_path = './Ner_model/final-model.pt'
WordList = './keyword2.txt'

x = extracrKeyWord(model_path,WordList)
print(x.extracNer_text(text)
```
