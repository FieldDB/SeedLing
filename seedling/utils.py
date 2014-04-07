# -*- coding: utf-8 -*-

def sync_and_read(url, filename):
  """ 
  Downloads and update a file from the given url, 
  if internet is available. 
  """
  import urllib2
  try: # Getting an updated version of the file online.
    infile = urllib2.urlopen(url).read().decode('utf8')
    with open(filename,'w') as fout:
      fout.write(infile)
  except urllib2.URLError:
    infile = open(filename, 'r').read()
  return infile

def parentdirectory():
  """ Returns parent directory. """
  import os
  return os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                      os.path.pardir))
  
