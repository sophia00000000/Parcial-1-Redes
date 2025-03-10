# Transformada de fourier en redes físicas



La Transformada de Fourier (TF) es una herramienta matemática fundamental en el análisis de señales en la capa física de las redes de comunicación. Su principal aporte es descomponer una señal en sus componentes de frecuencia, lo que permite entender y manipular la información de manera más eficiente en el dominio de la frecuencia.

A contribuido al análisis de señales en la capa física por medio de:
  - **La Conversión entre dominio del tiempo y dominio de la frecuencia:** Las señales en la capa física suelen transmitirse en el dominio del tiempo, pero muchas operaciones de procesamiento, como filtrado y modulación, se realizan de manera más eficiente en el dominio de la frecuencia. La TF permite esta conversión.
  - **Del Análisis de espectro y ancho de banda:** La TF permite determinar qué frecuencias componen una señal y evaluar su ancho de banda, lo que es crucial para evitar interferencias y optimizar el uso del espectro electromagnético.

Dada una señal en el dominio del tiempo x(t), su representación en el dominio de la frecuencia se obtiene mediante la Transformada de Fourier:

<p align="center">
  <img src="https://github.com/user-attachments/assets/0035d36b-7768-403e-9cc2-18c8cac1169d" alt="image" width="200">
</p>

Donde:
  - X(f) es la representación en frecuencia de la señal.
  - x(t) es la señal en el tiempo.
  - f es la frecuencia.
  - j es la unidad imaginaria (j²=1).

Esta transformación es crucial en la capa física para manipular y analizar señales en redes de comunicación.

## Aplicaciones

  ### 1. Filtrado de señales y reducción de ruido

En las telecomunicaciones, el ruido y las interferencias pueden degradar la señal transmitida. La TF permite identificar las frecuencias no deseadas y aplicar filtros para eliminarlas, mejorando la calidad de la transmisión.

Si tenemos una señal recibida con ruido:
<p align="center">
  <code>y(t) = x(t) + n(t)</code>
</p>


Donde: 
  - x(t) es la señal original.
  - n(t) es el ruido.

Cuando se aplica la transformada de fourier: 
<p align="center">
  <code>Y(f) = X(f) + N(f)</code>
</p>

Si el ruido N(f) está concentrado en ciertas frecuencias, podemos diseñar un filtro pasa-banda para eliminarlo. Un filtro ideal en el dominio de la frecuencia sería:
<p align="center">
  <img src="https://github.com/user-attachments/assets/99562bf0-871d-4a0f-8726-1f03966d861c" alt="image" width="200">
</p>

Una vez aplicado el filtro a la señal:
<p align="center">
  <code>x̅(f) = H(f)Y(f)</code>
</p>

Aplicamos la Transformada Inversa de Fourier (TIF)* para recuperar la señal en el dominio del tiempo:
<p align="center">
  <img src="https://github.com/user-attachments/assets/6c51caac-a0b8-4001-b703-81a1d0ea596f" alt="image" width="200">*
</p>

Este proceso ayuda a eliminar ruido fuera del rango de frecuencia útil y mejorar la calidad de la señal.

---

  ### 2. Multiplexación por División de Frecuencia Ortogonal (OFDM)

El OFDM (Orthogonal Frequency Division Multiplexing) es una técnica utilizada en Wi-Fi, LTE, 5G y DSL para mejorar la eficiencia espectral y la resistencia a interferencias.

En OFDM, los datos se transmiten en múltiples subportadoras ortogonales*. En lugar de enviar un solo flujo de datos a alta velocidad (lo que puede ser vulnerable a la interferencia), OFDM divide los datos en muchas subportadoras más lentas.

Cada símbolo OFDM se genera aplicando la Transformada Inversa de Fourier Discreta (IDFT):
<p align="center">
  <img src="https://github.com/user-attachments/assets/d183be32-f6f8-434b-bb2a-6ad1f7f04edf" alt="image" width="250">
</p>

Donde:
  - X[k] representa los símbolos de datos modulados en el dominio de la frecuencia.
  - x[n] es la señal en el dominio del tiempo.
  - N es el número de subportadoras.

La implementación eficiente de la IDFT en hardware y software se hace mediante la Transformada Rápida de Fourier (FFT).

En el receptor, se usa la Transformada de Fourier Discreta (DFT) para recuperar los símbolos:

<p align="center">
  <img src="https://github.com/user-attachments/assets/49ed958d-c3a1-41aa-991a-56651d3e7774" alt="image" width="200">*
</p>

Este proceso convierte la señal OFDM recibida nuevamente al dominio de la frecuencia (la TF normal) para demodular los datos.



## Aclaraciones

*(TIF) -> En el procesamiento de señales y telecomunicaciones, la Transformada de Fourier convierte una señal al dominio de la frecuencia para facilitar análisis y modificaciones. Luego, la Transformada Inversa de Fourier es clave para recuperar una señal en el dominio del tiempo después de procesarla en el dominio de la frecuencia.

*Tipo de señal continua -> Son funciones definidas para todo instante de tiempo (t) por lo que se trabaja con integrales.

*Una subportadora es una onda senoidal que transporta una parte de la información de la señal y dos señales son ortogonales si la integral de su producto en un período determinado es cero. Ej: Se tiene varias ondas senoidales **sin(2πf1t), sin(2πf2t), sin(2πf 3t), etc.** Si estas ondas tienen frecuencias no ortogonales, se mezclarían y crearían interferencia. Pero si están separadas por Δf=1/T, sus integrales de producto serán cero, asegurando que no interfieran.

*Tipo de señal discreta -> Solo están definidas en instantes específicos (n), no en todos los valores de tiempo, por lo que se trabaja con sumatorias.
