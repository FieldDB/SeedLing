SeedLing
========

Building and using a seed corpus for the *Human Language Project* (Steven and Abney, 2010).

The SeedLing corpus on this repository includes the data from:
*  **ODIN**: Online Database of Interlinear Text 
*  **Omniglot**: Useful foreign phrases from www.omniglot.com
*  **UDHR**: Universal Declaration of Human Rights

The SeedLing API includes scripts to access data/information from:
* **SeedLing**: different data sources that forms the SeedLing corpus (`odin.py`, `omniglot.py`, `udhr.py`, `wikipedia.py`)
* **ISO 639-3** : SIL ISO standards for language code (`miniethnologue.py`)
* **WALS**: Language information from World Atlas of Language Structures (`miniwals.py`)


To use the SeedLing corpus through the python API, please follow the instructions on the **Usage** section.

To download the plaintext version of the SeedLing corpus (excluding wikipedia data), click here.

To download the wikipedia data, please follow the **Getting Wikipedia** section.


To cite the SeedLing corpus:

`<authors>` . 2014. SeedLing: Building and using a seed corpus for the Human Language Project. In Proceedings of
*The use of Computational methods in the study of Endangered Languages (ComputEL) Workshop*. Baltimore, USA.

in `bibtex`:

```
@InProceedings{PustejovskyYocum:2013:IWCS2013:ISA-9,
  author    = {},
  title     = {SeedLing: Building and using a seed corpus for the Human Language Project},
  booktitle = {Proceedings of The use of Computational methods in the study of Endangered Languages (ComputEL) Workshop},
  month     = {JUne},
  year      = {2014},
  address   = {Baltimore, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {},
  url       = {}
}
```


***
Usage
=====

To access the SeedLing from various data sources:

```
from seedling import udhr, omniglot, odin

# Accessing ODIN IGTs:
>>> for lang, igts in odin.igts():
>>>   for igt in igts:
>>>     print lang, igt

# Accesing Omniglot phrases
>>> for lang, sent, trans in omniglot.phrases():
>>>   print lang, sent, trans

# Accessing UDHR sentences.
>>> for lang, sent in udhr.sents():
>>>   print lang, sent
```

To access the SIL and WALS information:

```
from seedling import miniwals, miniethnologue

# Accessing SIL ISO codes.
>>> sil = miniethnologue.MiniSIL()
>>> print sil.ISO6393['eng']
{'iso6391': u'en', 'name': u'English', 'iso6392t': u'eng', 'invert': u'English', 'ismacro': False, 'scope': 'Indvidual', 'type': 'Living', 'iso6392b': u'eng'}

# Accessing WALS information
>>> wals = miniwals.MiniWALS()
>>> print wals['eng']
{u'glottocode': u'stan1293', u'name': u'English', u'family': u'Indo-European', u'longitude': u'0.0', u'sample 200': u'True', u'latitude': u'52.0', u'genus': u'Germanic', u'macroarea': u'Eurasia', u'sample 100': u'True'}
```

Detailed usage of the API can also be found in `demo.py`.


***
Getting Wikipedia
====

***
References
====


