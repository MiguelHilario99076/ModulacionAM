
Sistema de Modulación en Amplitud (AM)
Descripción
Este proyecto implementa un sistema básico de Modulación en Amplitud (AM) utilizando Python. El objetivo es analizar el comportamiento de una señal modulada y estudiar los efectos del ruido, la atenuación y la distorsión en un sistema de comunicación.
La simulación genera una señal de información de baja frecuencia, la modula mediante una portadora de alta frecuencia y posteriormente realiza un análisis en el dominio del tiempo y de la frecuencia.


Objetivos

- Implementar un sistema de modulación AM.
- Analizar la señal modulada en el dominio temporal.
- Analizar el espectro de frecuencia mediante FFT.
- Evaluar el impacto del ruido sobre la señal transmitida.
- Observar los efectos de la atenuación y la distorsión.


Herramientas Utilizadas

- Python 3.12
- NumPy
- SciPy
- Matplotlib


Instalación
Instalar las dependencias necesarias:
pip install numpy scipy matplotlib


Ejecución
Ejecutar el programa desde la terminal:
python modulacion_am.py


Funcionamiento
El programa realiza las siguientes etapas:

1. Generación de una señal senoidal de baja frecuencia (mensaje).
2. Generación de una señal portadora de alta frecuencia.
3. Aplicación de la modulación AM.
4. Obtención del espectro mediante FFT.
5. Simulación de ruido gaussiano.
6. Simulación de atenuación de la señal.
7. Simulación de distorsión por saturación.
8. Visualización de resultados mediante gráficas.


Resultados Obtenidos
El programa genera las siguientes gráficas:

- Señal de información.
- Señal modulada AM.
- Espectro de frecuencia.
- Señal AM con ruido.
- Señal atenuada.
- Señal distorsionada.
Estas gráficas permiten observar cómo se comporta la señal durante la transmisión y cómo se ve afectada por distintas condiciones del canal.


Conclusiones
La modulación AM permite transmitir información mediante la variación de la amplitud de una señal portadora. Durante la simulación se comprobó que el ruido introduce perturbaciones aleatorias, la atenuación reduce la potencia de la señal y la distorsión altera su forma original. El análisis temporal y espectral permitió comprender el funcionamiento básico de los sistemas de comunicación analógicos.


Autor
Miguel Hilario
Actividad Formativa 4 - Sistemas de Comunicación y Modulación AM.
