from bs4 import BeautifulSoup as bs
from utils import parentdirectory


# If ethnologue language family html doesn't exist yet, download it.
if not os.path.exists(ETHNO_DIR+'ethnologue-family.html'):
  fin = urllib2.urlopen(ETHNOLOGUE_DOMAIN+'browse/families')\
        .read().decode('utf8')
  with codecs.open(ETHNO_DIR+'ethnologue-family.html','w','utf8') as fout:
    print>>fout, fin

fin = codecs.open(ETHNO_DIR+'ethnologue-family.html','r','utf8')
lang_fams = defaultdict(list)

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