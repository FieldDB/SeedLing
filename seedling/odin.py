# -*- coding: utf-8 -*-

# Access modules from parent dir, see http://goo.gl/dZ5HVk
import os, sys
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

import tarfile, codecs, os, re, string, shutil
from collections import defaultdict
import cPickle as pickle
from utils import remove_tags, make_tarfile, read_tarfile

try:
  from bs4 import BeautifulSoup as bs
except:
  from BeautifulSoup import BeautifulSoup as bs
#bs.find_all = getattr(bs, 'find_all',False) or getattr(bs, 'findAll')


def get_odin_igts(ODINFILE=parentddir+'/data/odin/odin-full.tar'):
  """
  Extracts the examples from the ODIN igts and returns a defaultdict(list),
  where the keys are the lang iso codes and values are the examples.
  
  >>> igts = get_odin_igts()
  >>> for lang in igts:
  >>>  for igt in igts[lang]:
  >>>    print lang, igt
  """
  
  tar = tarfile.open(ODINFILE)
  docs = defaultdict(list)
  for infile in tar:
    if '.xml' in infile.name: # there's a rogue file in the tar that is not xml.
      lang = infile.name[:-4].lower()
      ##print lang
      # Find the <igt>...</igt> in the xml.
      odinfile = tar.extractfile(infile).read()
      igts = bs(odinfile).findAll('igt')
      citations = bs(odinfile).findAll('citation')
      for igt, cite in zip(igts, citations):        
        # Find the <example>...</example> in the igt.
        examples = bs(unicode(igt)).findAll('example')
        cite = remove_tags(unicode(cite)).strip(' &lt;/p&gt;')
        for eg in examples:
          try:
            # Only use triplets lines and assumes that
            # line1: src, line2:eng, line3:gloss
            src, eng, gloss = bs(unicode(eg)).findAll('line')
            src, eng, gloss, cite = map(unicode, [src, eng, gloss, cite])
            docs[lang].append((src, eng, gloss, cite))
            ##print src, eng, gloss, cite
          except:
            raise; print eg
  return docs

def load_odin_pickle(ODIN_PICKLE=parentddir+'/data/odin/odin-docs.pk'):
  """
  Loads odin-docs.pk and yield one IGT at a time.
  
  >>> for lang, igts in load_odin_pickle():
  >>>   for igt in igts:
  >>>     print lang, igt
  """
  # If odin-docs.pk is not available create it.
  if not os.path.exists(ODIN_PICKLE):
    odindocs = get_odin_igts()
    # Outputs the odin igts examples into '../data/odin/odin-docs.pk'.
    with codecs.open(ODIN_PICKLE,'wb') as fout:
      pickle.dump(odindocs, fout)  
      
  # Loads the pickled file.
  with codecs.open(ODIN_PICKLE,'rb') as fin2: 
    docs = pickle.load(fin2)
    for lang in docs:
      # the data might be too much for the RAM, so yield instead of return.
      yield (lang, docs[lang])
 
def igts():
  """ Yields IGTs from ODIN. """
  for lang, examples in load_odin_pickle():
    yield lang, examples
    
def source_sents(intarfile=parentddir+'/data/odin/odin-all.tar'):
  """ Yield clean sentences from the clean ODIN tarball. """
  for infile in sorted(read_tarfile(intarfile)):
    language = infile.split('/')[-1].split('-')[1].split('.')[0].split('_')[0]
    with codecs.open(infile,'r','utf8') as fin:
      for line in fin.readlines():
        sentence = line.strip().split('\t')[0]
        yield language, sentence
        
def languages():
  """Returns the number of languages available from original data source."""
  return [str(i.name).partition('.')[0] \
          for i in tarfile.open(parentddir+'/data/odin/odin-full.tar')]

def num_languages():
  """ Returns the number of languages available from original data source. """
  return len(languages())
