# -*- coding: utf-8 -*-

from seedling import miniwals, miniethnologue
from seedling import udhr, omniglot, odin

# Accessing WALS information
wals = miniwals.MiniWALS()
print wals['eng']
print sorted(wals.LANGUAGEFAMILY.keys())
print wals.LANGUAGEFAMILY['Indo-European']
print wals.GENUS['Germanic']
print sorted(wals.RELATED_LANGS['eng'])

# Accessing SIL ISO codes.
sil = miniethnologue.MiniSIL()
print sil.ISO6393['eng']
print sil.name2code('German')
for i in sil.MACROLANGS:
  print i, sil.MACROLANGS[i], len(sil.MACROLANGS[i]), sil.ISO6393[i]

# Checking language code status from SIL.
check_lang_status = miniethnologue.check_lang()
print check_lang_status('eng',"Status")
print check_lang_status('lnc',"Status")

# Accessing UDHR sentences.
print udhr.languages()
print udhr.num_languages()
for lang, sent in udhr.source_sents():
  print lang, sent
  
# Accessing Omniglot sentences.
print omniglot.languages()
print omniglot.num_languages()
for lang, sent, trans in omniglot.phrases():
  print lang, sent, trans

# Accessing ODIN sentences.
print odin.languages()
print odin.num_languages()
for lang, sent in odin.source_sents():
  print lang, sent
for lang, igts in odin.igts():
  for igt in igts:
    print lang, igt
