# -*- coding: utf-8 -*-

from collections import defaultdict
from utils import sync_and_read

WALS_URL = "http://wals.info/languoid.tab?sEcho=1&iSortingCols=1"+\
            "&iSortCol_0=0&sSortDir_0=asc"
WALS_TXT = "data/wals.txt"
            
wals_tsv = sync_and_read(WALS_URL, WALS_TXT)  
headerline, _ , data = wals_tsv.partition('\n')

WALS = {}
for line in data.split('\n'):
  lang = line.split()[0]
  for key, value in zip(headerline.split()[1:], line.split()[1:]):
    WALS.setdefault(lang,{})[key] = value
    
LANG2FAMILY = defaultdict(list)
for lang in WALS:
  LANG2FAMILY[WALS[lang]['genus']].append(lang)

RELATED_LANGS = defaultdict(list)
for lang in WALS:
  RELATED_LANGS[lang] = LANG2FAMILY[WALS[lang]['genus']]
