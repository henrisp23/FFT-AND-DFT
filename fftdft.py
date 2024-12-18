import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


sampling_rate = 3000  
T = 1 / sampling_rate  
duration = 1  
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  
freq1 = 50  
freq2 = 120  
signal = 5 * np.sin(2 * np.pi * freq1 * t) + 3 * np.sin(2 * np.pi * freq2 * t) + np.random.normal(0, 0.5, t.shape)

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X


fft_result = fft(signal)
dft_result = dft(signal)


frequencies = np.fft.fftfreq(len(signal), T)


fft_magnitude = np.abs(fft_result)
dft_magnitude = np.abs(dft_result)


plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Time-Domain Signal', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Oscilloscope Signal')
plt.legend()
plt.grid()


plt.subplot(3, 1, 2)
plt.stem(frequencies[:len(frequencies) // 2], fft_magnitude[:len(frequencies) // 2], label='FFT', linefmt='r-', markerfmt='ro', basefmt='r-')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of the Signal')
plt.legend()
plt.grid()


plt.subplot(3, 1, 3)
plt.stem(frequencies[:len(frequencies) // 2], dft_magnitude[:len(frequencies) // 2], label='DFT', linefmt='g-', markerfmt='go', basefmt='g-')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('DFT of the Signal')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
