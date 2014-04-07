# -*- coding: utf-8 -*-

from collections import defaultdict
import urllib2

WALS_URL = "http://wals.info/languoid.tab?sEcho=1&iSortingCols=1"+\
            "&iSortCol_0=0&sSortDir_0=asc"
WALS_TXT = "wals.txt"
            
try: # Getting an updated version of WALS online.
  wals_tsv = urllib2.urlopen(WALS_URL).read()
  with open(WALS_TXT,'w') as fout:
    fout.write(wals_tsv)
except urllib2.URLError:
  wals_tsv = open(WALS_TXT, 'r').read()
  
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