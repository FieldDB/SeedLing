# -*- coding: utf-8 -*-

import cPickle as pickle
import codecs
from utils import sync_and_read


ETHNOFAMILY_URL = "http://www.ethnologue.com/browse/families"
ETHNOFAMILY_HTML = "data/ethnologue/ethnologue-family.html"

sync_and_read(ETHNOFAMILY_URL, ETHNOFAMILY_HTML)

x = pickle.load(codecs.open('data/ethnologue/languages_with_info.pk','rb'))

for i in x:
  for j in x[i]:
    print i, j




"""
fin = codecs.open(ETHNO_DIR+'ethnologue-family.html','r','utf8')
lang_fams = defaultdict(list)
"""

"""
for line in fin.readlines():
  line = line.decode('utf-8')
  # Detects the language family and its link.
  if LANG_FAMILY_TAG in line:
    langfamlink = bs(line).find('a').get('href')
    langfamily = bs(line).get_text().strip()
    print langfamily, langfamlink
    # Downloads the page of a language family and gets its:
    # (1) name, (2) iscode (3) geographical information
    for line2 in urllib2.urlopen(ETHNOLOGUE_DOMAIN+langfamlink):
      line2 = line2.decode('utf-8')
      if LANG_TAG in line2:
        lang = bs(line2).get_text().strip()
        if lang.strip() == "": continue
        langname = re.sub(r'[\[\(\<][^)]*[\]\)\>]', '', lang)
        isocode = re.findall(r'\[([^]]*)\]',lang)[0]
        geo = re.findall(r'\([^)]*\)',lang)[0].rpartition(" ")[2][:-1]
        ##print isocode, langname , geo
        lang_fams[langfamily].append((isocode, langname , geo, langfamlink))
"""