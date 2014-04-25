# -*- coding: utf-8 -*-

import cPickle as pickle
from collections import defaultdict

import udhr, omniglot, odin, wikipedia
from counting import count_living_languages, pseudo_ethnologue, sil


for resource in ['udhr', 'omniglot', 'odin', 'wikipedia']:
  livinglanguages = count_living_languages(resource, True)
  endangerment_languages = defaultdict(list)
  for i in livinglanguages:
    if i in ["nob","nno"]: i = "nor"
    endangerment_level = pseudo_ethnologue[i][0][-1].split()[0]
    endangerment_languages[endangerment_level].append(i)
  
  print resource
  for endangerment, languages in sorted(endangerment_languages.iteritems()):
    print endangerment+"\t"+str(len(languages))
  print