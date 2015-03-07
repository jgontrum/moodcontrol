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

cleanedTimeArray = clean(timeArray, 40)

print "Max: ", numpy.max(cleanedTimeArray)
print "Min: ", cleanedTimeArray.min()
print "Mean: ", cleanedTimeArray.mean()
print "PeakToPeak: ", cleanedTimeArray.ptp()
print "Variance: ", numpy.var(cleanedTimeArray)
print "Median: ", numpy.median(cleanedTimeArray)
print "Std Abweicheung: ", numpy.std(cleanedTimeArray)
print "Cov: ", numpy.cov(cleanedTimeArray)

plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
#show()

#### Plotting the Frequency Content
n = len(s1) 
nUniquePts = ceil((n+1)/2.0)

p = abs(fft(s1)[0:nUniquePts])

p = p / float(n) # scale by the number of points so that
                 # the magnitude does not depend on the length 
                 # of the signal or on its sampling frequency  
p = p**2  # square it to get the power 

# multiply by two (see technical document for details)
# odd nfft excludes Nyquist point
if n % 2 > 0: # we've got odd number of points fft
    p[1:len(p)] = p[1:len(p)] * 2
else:
    p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);

plot(freqArray/1000, 10*log10(p), color='k')

cleanedfreqArray = freqArray

# print "Max: ", cleanedfreqArray.max()
# print "Min: ", cleanedfreqArray.min()
# print "Mean: ", cleanedfreqArray.mean()
# print "PeakToPeak: ", cleanedfreqArray.ptp()
# print "Variance: ", numpy.var(cleanedfreqArray)
# print "Median: ", numpy.median(cleanedfreqArray)
# print "Std Abweicheung: ", numpy.std(cleanedfreqArray)
# print "Cov: ", numpy.cov(cleanedfreqArray)
# print "--"
