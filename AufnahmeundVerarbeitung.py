#PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
import os
from pylab import*
from scipy.io import wavfile
from scipy import stats
import numpy
import sys
import re

def clean(array, threshold):
	cleanedList = []
	for i in array:
		if i > threshold:
			cleanedList.append(i)
	return numpy.array(cleanedList)
    
def aufnahme():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return wf

def analyse():
        wf = aufnahme()

        sampFreq, snd = wavfile.read("output.wav")

        bits = int(re.findall(r'\d+',str(snd.dtype))[0]) - 1
        # 16bit Audio:
        print float(list(snd.shape)[0])
        snd = snd / (2.**bits)

        # Channel 1 only
        s1 = snd[:,0]

        cleanedTimeArray = s1

        print "Max", numpy.max(cleanedTimeArray)
        print "Min", cleanedTimeArray.min()
        print "Mean", cleanedTimeArray.mean()
        print "PTP", cleanedTimeArray.ptp()
        print "Var", numpy.var(cleanedTimeArray)
        print "Median", numpy.median(cleanedTimeArray)
        print "Std", numpy.std(cleanedTimeArray)
        print "Cov", numpy.cov(cleanedTimeArray)
        print "Integral", cleanedTimeArray.sum() / (float(list(snd.shape)[0])/sampFreq)


        #### Plotting the tone
        timeArray = arange(0, float(list(snd.shape)[0]), 1)
        timeArray = timeArray / sampFreq
        timeArray = timeArray * 1000  #scale to milliseconds
        plot(timeArray, s1, color='k')
        ylabel('Amplitude')
        xlabel('Time (ms)')
        #show()

        return cleanedTimeArray.sum() / (float(list(snd.shape)[0])/sampFreq)
