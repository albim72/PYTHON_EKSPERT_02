import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100

samplingInterval = 1/samplingFrequency
beginTime = 0
endTime = 10

singnal1Frequency = 4
singnal2Frequency = 7

time = np.arange(beginTime,endTime,samplingInterval)

amplitude1 = np.sin(2*np.pi*singnal1Frequency*time)
amplitude2 = np.sin(2*np.pi*singnal2Frequency*time)

figure,axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)
#wykres 1 funkcji falowej 4Hz
axis[0].set_title('funkcja falowa o częstotliwości 4Hz')
axis[0].plot(time,amplitude1)
axis[0].set_xlabel('Czas')
axis[0].set_ylabel('Amplituda')

#wykres 2 funkcji falowej 7Hz
axis[1].set_title('funkcja falowa o częstotliwości 7Hz')
axis[1].plot(time,amplitude2)
axis[1].set_xlabel('Czas')
axis[1].set_ylabel('Amplituda')

#złożenie funckji falowych -> wykres
amplitude = amplitude1 + amplitude2

axis[2].set_title('złożenie dwóch funkcji falowych: amp1 i amp2')
axis[2].plot(time,amplitude)
axis[2].set_xlabel('Czas')
axis[2].set_ylabel('Amplituda')

#Transformata Fouriera
fourierTransform = np.fft.fft(amplitude)/len(amplitude) #normalizacja
fourierTransform = fourierTransform[range(int(len(amplitude)/2))]

tpCount = len(amplitude)
values = np.arange(int(tpCount/2))
timePeriod = tpCount/samplingFrequency
frequencies = values/timePeriod

#wykres transformaty Fouriera dla funkcji amplitude
axis[3].set_title('transformata Fouriera dla amplitude')
axis[3].plot(frequencies,abs(fourierTransform))
axis[3].set_xlabel('Częstotliwość')
axis[3].set_ylabel('Amplituda')

plt.show()

