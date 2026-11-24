# =====================================================
# Actividad Formativa 4
# Modulación en Amplitud (AM)
# Autor: Miguel Hilario
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# =====================================================
# 1. Definición de parámetros
# =====================================================

fs = 10000          # Frecuencia de muestreo (Hz)
T = 0.05            # Duración de la señal (s)

t = np.arange(0, T, 1/fs)

fm = 100            # Frecuencia del mensaje (Hz)
fc = 1000           # Frecuencia portadora (Hz)
mu = 0.8            # Índice de modulación

# =====================================================
# 2. Señal de entrada (mensaje)
# =====================================================

mensaje = np.sin(2 * np.pi * fm * t)

# =====================================================
# 3. Portadora
# =====================================================

portadora = np.cos(2 * np.pi * fc * t)

# =====================================================
# 4. Modulación AM
# s(t) = (1 + mu*m(t))*c(t)
# =====================================================

senal_am = (1 + mu * mensaje) * portadora

# =====================================================
# 5. Introducción de ruido
# =====================================================

ruido = 0.3 * np.random.randn(len(t))

senal_ruidosa = senal_am + ruido

# =====================================================
# 6. Atenuación
# =====================================================

factor_atenuacion = 0.5

senal_atenuada = factor_atenuacion * senal_am

# =====================================================
# 7. Distorsión (saturación)
# =====================================================

senal_distorsionada = np.clip(senal_am, -0.8, 0.8)

# =====================================================
# 8. Análisis en frecuencia mediante FFT
# =====================================================

N = len(t)

yf = fft(senal_am)
xf = fftfreq(N, 1/fs)

indices = xf > 0

# =====================================================
# 9. Gráficas
# =====================================================

plt.figure(figsize=(14,10))

# Señal mensaje
plt.subplot(3,2,1)
plt.plot(t, mensaje)
plt.title("Señal de Información")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

# Señal AM
plt.subplot(3,2,2)
plt.plot(t, senal_am)
plt.title("Señal Modulada AM")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

# Espectro
plt.subplot(3,2,3)
plt.plot(xf[indices], np.abs(yf[indices]))
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()

# Señal con ruido
plt.subplot(3,2,4)
plt.plot(t, senal_ruidosa)
plt.title("Señal AM con Ruido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

# Señal atenuada
plt.subplot(3,2,5)
plt.plot(t, senal_atenuada)
plt.title("Señal Atenuada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

# Señal distorsionada
plt.subplot(3,2,6)
plt.plot(t, senal_distorsionada)
plt.title("Señal Distorsionada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.show()