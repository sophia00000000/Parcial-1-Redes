import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# Parámetros de la señal
fs = 1000  # Frecuencia de muestreo (Hz)
T = 1      # Duración de la señal (segundos)
t = np.linspace(0, T, fs, endpoint=False)  # Vector de tiempo

# Frecuencias de las sinusoides
f1, f2, f3 = 50, 150, 300  # Hz
A1, A2, A3 = 1.0, 0.8, 0.6  # Amplitudes

# Señal en el dominio del tiempo
x_t = A1 * np.cos(2 * np.pi * f1 * t) + A2 * np.cos(2 * np.pi * f2 * t) + A3 * np.cos(2 * np.pi * f3 * t)

# Aplicamos la Transformada de Fourier
X_f = fft(x_t)
freqs = fftfreq(fs, 1/fs)  # Frecuencias correspondientes

# Graficamos la señal en el dominio del tiempo
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x_t)
plt.title("Señal en el dominio del tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()

# Graficamos la magnitud de la Transformada de Fourier (dominio de la frecuencia)
plt.subplot(1, 2, 2)
plt.stem(freqs[:fs//2], np.abs(X_f[:fs//2]) / (fs//2), use_line_collection=True)
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.show()
