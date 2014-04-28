# -*- coding: utf-8 -*-

import codecs, re
from collections import defaultdict
from utils import sync_and_read, currentdirectory

# Link to the ISO 639-3 file.
ISO6393_URL = "http://www-01.sil.org/iso639-3/iso-639-3.tab"
ISO6393_TXT = currentdirectory()+"/data/sil/iso6393.txt"
# Link to the ISO 639-3 names file.
ISO6393_NAME_URL = "http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab"
ISO6393_NAME_TXT = currentdirectory()+"/data/sil/iso6393-name.txt" # a local copy.
# Scope of language, http://www-01.sil.org/iso639-3/scope.asp
# Type of language, see http://www-01.sil.org/iso639-3/types.asp
# See http://www-01.sil.org/iso639-3/iso-639-3.tab
scopetype = {"I":"Indvidual", "M":"Macrolanguage",
               "L":"Living", "E":"Extinct", "A":"Ancient", 
               "H":"Historic", "C":"Constructed"}
# Link to ISO 639-3 Macrolanguages file.
MACROLANGS_URL = "http://www-01.sil.org/iso639-3/iso-639-3-macrolanguages.tab"
MACROLANGS_TXT = currentdirectory()+"/data/sil/marcolangs.txt" # a local copy.

# Link to the ISO 639-3 retirement file. 
RETIRED_URL = "http://www-01.sil.org/iso639-3/iso-639-3_Retirements.tab"
RETIRED_TXT = currentdirectory()+"/data/sil/retired.txt" # a local copy.

class MiniSIL:
  def __init__(self, toupdate=True):
    
    self.ISO6393, self.MARCOLANGS = {} , defaultdict(list)
    self.update(toupdate)
  
  def update(self, toupdate=True):
    """ Updates the ISO 639-3, if internet connection is available. """
    # Saving contents from iso-639-3.tab into ISO6393 object.
    iso6393_tsv = sync_and_read(ISO6393_URL, 
                                ISO6393_TXT, toupdate=toupdate)
    iso6393_data = iso6393_tsv.partition('\n')[2] # Removes headerlines.
    headerline = "iso6392t iso6392b iso6391 scope type name comment"

    for i in iso6393_data.split('\n'):
      code, _, i = i.strip().partition('\t')
      for value, column in zip(i.split('\t'), headerline.split()):
        if value in scopetype: value = scopetype[value];
        self.ISO6393.setdefault(code,{})[column]= value
    
    # Saving contents from iso-639-3_Name_Index.tab into ISO6393 object.
    iso6393name_tsv = sync_and_read(ISO6393_NAME_URL, 
                                    ISO6393_NAME_TXT, toupdate=toupdate)
    iso6393name_data = iso6393name_tsv.partition('\n')[2] # Removes headerlines.

    for i in iso6393name_data.split('\n'):
      code, name, invert = i.strip().split('\t')
      ismacrolang = True if "(macrolanguage)" in name else False
      self.ISO6393[code]["name"]= name
      self.ISO6393[code]["invert"] = invert
      self.ISO6393[code]["ismacro"] = ismacrolang
    
    # Saving contents from iso-639-3-macrolanguages.tab into *MACROLANGS*.
    marcolang_tsv = sync_and_read(MACROLANGS_URL, MACROLANGS_TXT, \
                                  toupdate=toupdate)
    macrolang_data = marcolang_tsv.partition('\n')[2]
    
    self.MACROLANGS = defaultdict(list)
    for i in macrolang_data.split('\n'):
      macro, code, status = i.strip().split('\t')
      status = "Active" if status == "A" else "Retired"
      self.ISO6393.setdefault(code, {})["macro"] =  macro
      self.ISO6393.setdefault(code, {})["status"] =  status
      self.MACROLANGS[macro].append(code)
      
  
    # Saving contents from iso-639-3_Retirements.tab into *RETIRED*.
    retired_tsv = sync_and_read(RETIRED_URL, RETIRED_TXT, toupdate=toupdate)
    retired_data = retired_tsv.partition('\n')[2]
    
    self.RETIRED = defaultdict(list)
    for i in retired_data.split('\n'):
      "Id  Ref_Name  Ret_Reason  Change_To  Ret_Remedy  Effective"
      code, refname, reason, changeto, \
      remedy, effectivedate = i.strip().split('\t')
      
      if reason == "S" and "Split into" in remedy:
        changeto = "_".join(re.findall(r"\[(.*?)\]", remedy)) 
      
      self.ISO6393.setdefault(code, {})["retired"] = True
      self.ISO6393.setdefault(code, {})["changeto"] = changeto
  
      
  def name2code(self, language_name):
    for i in self.ISO6393:
      try:
        if self.ISO6393[i]['name'].lower() == language_name.lower():
          return i
      except KeyError:
        pass
        ##print i, self.ISO6393[i]

def check_lang(langcode, option):
  """ Queries SIL website for language status given the language code. """
  import urllib2, re
  from bs4 import BeautifulSoup as bs
  from utils import remove_tags
  url = "http://www-01.sil.org/iso639-3/documentation.asp?id="+langcode
  page = urllib2.urlopen(url).read().decode('utf8')
  if "The supplied value for the code parameter is not "+\
  "a valid three-letter identifier." in page:
    return None
  status = unicode([i for i in bs(page).\
            find_all('tr') if option+":" in i.text][0])
  status = re.findall(r'<td>.*?<\/td>', status)[0]
  return remove_tags(status).lower()


'''# USAGE:
minisil = MiniSIL()

print minisil.ISO6393['eng']
for i in minisil.MACROLANGS:
  print i, minisil.MACROLANGS[i], len(minisil.MACROLANGS[i]), minisil.ISO6393[i]
'''

'''
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
'''

