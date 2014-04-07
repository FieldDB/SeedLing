# -*- coding: utf-8 -*-

import codecs, re
from collections import defaultdict
from utils import sync_and_read

ISO6393_URL = "http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab"
ISO6393_TXT = "data/iso6393.txt"

iso6393_tsv = sync_and_read(ISO6393_URL, ISO6393_TXT)
iso6393_data = iso6393_tsv.partition('\n')[2]

ISO6393 = {}
for i in iso6393_data.split('\n'):
  code, name, invert = i.strip().split('\t')
  ismarcolang = True if "(macrolanguage)" in name else False
  ISO6393.setdefault(code,{})["name"]= name
  ISO6393.setdefault(code,{})["invert"] = invert
  ISO6393.setdefault(code,{})["macro"] = ismarcolang
  
###################################################################

MACROLANGS_URL = "http://www-01.sil.org/iso639-3/iso-639-3-macrolanguages.tab"
MACROLANGS_TXT = "data/marcolangs.txt"

marcolang_tsv = sync_and_read(MACROLANGS_URL, MACROLANGS_TXT)
macrolang_data = marcolang_tsv.partition('\n')[2]

MACROLANGS = defaultdict(list)
for i in macrolang_data.split('\n'):
  macro, lang, status = i.strip().split('\t')
  status = "Active" if status == "A" else "Retired"
  ISO6393.setdefault(lang, {})["macro"] =  macro
  ISO6393.setdefault(lang, {})["status"] =  status
  MACROLANGS[macro].append(lang)
  
###################################################################



###################################################################

CONLANG = {"ido":"Ido","tlh":"Klingon","tzl":"Talossan","jbo":"Lojban",
          "ina":"Interlingua","nov":"Novial", "arc":"Imperial Aramaic",
          "got":"Gothic","ile":"Interlingue","vol":"Volapük"}

DEADLANG = {"osp":"Old Spanish", "odt":"Old Dutch", "goh": "Old High German",
        "got":"Gothic","wlm":"Middle Welsh","oge":"Old Georgian",
        "tpn":"Tupinamba","ojp":"Old Japanese","sga":"Old Irish",
        "hit":"Hittite","tkm":"Takelma","dum":"Middle Dutch",
        "fro":"Old French","nci":"Classical Nahuatl","gmh":"Middle High German",
        "mxi":"Mozarabic", "ang": "Old English", "lzh": "Literary Chinese"}

####################################################################
  

