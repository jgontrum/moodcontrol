#!/usr/bin/python
import os
from scipy.io import wavfile

#Load *.WAV-file(s)
#loads a single *.wav file or all *.wav files in a directory
#argument:	file- or directory name
#returns:	list with content of loaded wav file(s) as strange type of wavfile.read()
def load(name):
  if os.path.isfile(name) == True:
    daten = [wavfile.read(filey)]
  elif os.path.isdir(name) == True:
    daten = []
    for filey in os.listdir(name):
      if filey.endswith('.WAV') or filey.endswith('.wav'):
	daten.append(wavfile.read(filey))
  else:
    print 'error:\n\''+name+'\' is no file or directory'
  print len(daten),'wav-file(s) sucessfully loaded!'
  return daten