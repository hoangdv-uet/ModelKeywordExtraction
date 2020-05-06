# Keyword Extraction by NER model combine with Keyword

### Requirement:
    * flar
    * pandas
    * numpy
    * bs4
    * re
    * string

Need to download [this model](https://drive.google.com/drive/folders/1QQQGnK4-FoPRueYO6PSPeosGA-IyQRgr?usp=sharing)!

### How to get entities:
```python
from KeyWordExtraction import *

text = 'Bill Gate'
model_path = './Ner_model/final-model.pt'
WordList = './keyword2.txt'

x = extracrKeyWord(model_path,WordList)
print(x.extracNer_text(text)
```
