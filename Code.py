import scipy as sc
import scipy.signal as sg
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
[Rate, Signal] = wav.read('salam.wav')  # Reading the sound file
L = [i for i in range(Rate//16)]  # X-axis variable
plt.subplot(3, 1, 1)
plt.stem(L, Signal[:Rate//16])  # Plotting voice signal
plt.ylabel('The Original Signal')
X = np.zeros(8001)
X[0] = 1
X[8000] = 0.7  # Creation of the signal that will cause the echo
Echo = sc.convolve(X, Signal)  # Creating Echo by conv
Echo = np.ndarray.astype(Echo, "int16")  # To convert the array from float to integer
plt.subplot(3, 1, 2)
plt.stem(L, Echo[:Rate//16])  # Plotting Echo signal
plt.ylabel('Signal with echo')
wav.write('Echo.wav', Rate, Echo)
Removed = sg.deconvolve(Echo, X)  # Obtaining the original signal by deconv
printed = np.ndarray.astype(Removed[0], "int16")  # To convert the array from float to integer
plt.subplot(3, 1, 3)
plt.stem(L, printed[:Rate//16])  # Plotting signal after removing echo effect
plt.ylabel('After Removing')
wav.write('Fixed.wav', Rate, printed)
plt.show()
