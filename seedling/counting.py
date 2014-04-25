# -*- coding: utf-8 -*-

import cPickle as pickle
import codecs

import udhr, omniglot, odin, wikipedia
import miniwals, miniethnologue
from miniethnologue import check_lang


sil = miniethnologue.MiniSIL(toupdate=False)

pkfile = 'data/ethnologue/livinglanguages_with_info.pk'
pseudo_ethnologue = pickle.load(codecs.open(pkfile, 'rb'))


livinglanguages_in_seedling = set()
for resource in ['udhr', 'omniglot', 'odin', 'wikipedia']:  
  languages = globals()[resource].languages()
  languages_iso6393 = [i for i in languages if i in sil.ISO6393] 
  num_in_ISO = len(languages_iso6393)
  #not_in_ISO = {i:check_lang(i, option="Status") for i in \
  #              set(languages).difference(languages_iso6393)}
  livinglanguages = [i for i in languages_iso6393 if i in \
                     pseudo_ethnologue.keys()+['nno', 'nob']]
  not_living = {}
  for i in set(languages_iso6393).difference(livinglanguages):
    if i in sil.MACROLANGS:
      not_living[i] = "macro"
    else:
      langtype = check_lang(i, option="Type")
      if check_lang(i, option="Type") == '' and \
      check_lang(i, option="Status") == "retired":
        langtype = "retired"  
      not_living[i] = langtype
    
  print resource
  print "Original #Languages :", len(languages)
  print "#Languages in ISO:", num_in_ISO
  print "#LivingLanguages:", len(livinglanguages)
  ##print "Languages not in ISO:", not_in_ISO
  ##print not_living
  print
  
  livinglanguages_in_seedling.update(livinglanguages)

print "Combined #Languages:", len(livinglanguages_in_seedling)