# Transformada de fourier en redes físicas



La Transformada de Fourier (TF) es una herramienta matemática fundamental en el análisis de señales en la capa física de las redes de comunicación. Su principal aporte es descomponer una señal en sus componentes de frecuencia, lo que permite entender y manipular la información de manera más eficiente en el dominio de la frecuencia.

A contribuido al análisis de señales en la capa física por medio de:
  - La Conversión entre dominio del tiempo y dominio de la frecuencia: Las señales en la capa física suelen transmitirse en el dominio del tiempo, pero muchas operaciones de procesamiento, como filtrado y modulación, se realizan de manera más eficiente en el dominio de la frecuencia. La TF permite esta conversión.
  - Del Análisis de espectro y ancho de banda: La TF permite determinar qué frecuencias componen una señal y evaluar su ancho de banda, lo que es crucial para evitar interferencias y optimizar el uso del espectro electromagnético.

Dada una señal en el dominio del tiempo x(t), su representación en el dominio de la frecuencia se obtiene mediante la Transformada de Fourier:

<p align="center">
  <img src="https://github.com/user-attachments/assets/0035d36b-7768-403e-9cc2-18c8cac1169d" alt="image">
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

`y(t) = x(t) + n(t)`

Donde: 
  - x(t) es la señal original.
  - n(t) es el ruido.

Cuando se aplica la transformada de fourier: 

`Y(f) = X(f) + N(f)`

Si el ruido N(f) está concentrado en ciertas frecuencias, podemos diseñar un filtro pasa-banda para eliminarlo. Un filtro ideal en el dominio de la frecuencia sería:

`H(f) = { 1, si f ∈ [f1, f2]  
        0, fuera de esa banda }`


