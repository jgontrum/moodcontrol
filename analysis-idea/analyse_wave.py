from pylab import*
from scipy.io import wavfile
from scipy import stats
import numpy
import sys
import re

# See: http://samcarcagno.altervista.org/blog/basic-sound-processing-python/



def clean(array, threshold):
	cleanedList = []
	for i in array:
		if i > threshold:
			cleanedList.append(i)
	return numpy.array(cleanedList)

if len(sys.argv) != 2:
	print "Argument: Path to wave"
	sys.exit(1)

# Read in
try:
	sampFreq, snd = wavfile.read(sys.argv[1])
except Exception, e:
	print e
	sys.exit(1)

bits = int(re.findall(r'\d+',str(snd.dtype))[0]) - 1
# 16bit Audio:
snd = snd / (2.**bits)

# Channel 1 only
s1 = snd[:,0] 

#### Plotting the tone
timeArray = arange(0, float(list(snd.shape)[0]), 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

cleanedTimeArray = s1

print sys.argv[1]
print cleanedTimeArray.sum() / (float(list(snd.shape)[0]) / sampFreq)

<<<<<<< HEAD
# print numpy.max(cleanedTimeArray)
# print cleanedTimeArray.min()
# print cleanedTimeArray.mean()
=======
print cleanedTimeArray.sum() / 1000000

print numpy.max(cleanedTimeArray)
#print cleanedTimeArray.min()
print cleanedTimeArray.mean()
>>>>>>> f9b6ac8d1009ed19733ba378412a6080a5c25b3d
# print cleanedTimeArray.ptp()
# print numpy.var(cleanedTimeArray)
# print numpy.median(cleanedTimeArray)
# print numpy.std(cleanedTimeArray)
# print numpy.cov(cleanedTimeArray)
# print cleanedTimeArray.sum()

plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
show()
