# Punto 3: Comportamiento de TCP ante Congestión de Red

Simulación en Python para representa el comportamiento de la ventana de congestión (cwnd) de TCP en función de eventos simulados de éxito o pérdida de paquetes.

- Inicialmente, la ventana de congestión (cwnd) tiene un valor de 1.
- Por cada transmisión exitosa (simulada), el valor de la ventana debe incrementarse en uno.<code> cwnd += 1 </code>
- Si ocurre una pérdida de paquete, la ventana de congestión debe reducirse drásticamente (similar a un reinicio a la fase de Slow Start). <code> cwnd = 1 </code>

Simulación de 20 transmisiones, donde cada transmisión puede tener éxito (probabilidad del 80%) o fallar (probabilidad del 20%).

    exito = random.randint(1, 100) <= 80 

  
---
### Salida 

    Transmisión 1: Exito, cwnd=2
    Transmisión 2: Pérdida, cwnd=1
    Transmisión 3: Pérdida, cwnd=1
    Transmisión 4: Exito, cwnd=2
    Transmisión 5: Exito, cwnd=3
    Transmisión 6: Exito, cwnd=4
    Transmisión 7: Exito, cwnd=5
    Transmisión 8: Pérdida, cwnd=1
    Transmisión 9: Pérdida, cwnd=1
    Transmisión 10: Exito, cwnd=2
    Transmisión 11: Exito, cwnd=3
    Transmisión 12: Pérdida, cwnd=1
    Transmisión 13: Exito, cwnd=2
    Transmisión 14: Exito, cwnd=3
    Transmisión 15: Exito, cwnd=4
    Transmisión 16: Pérdida, cwnd=1
    Transmisión 17: Pérdida, cwnd=1
    Transmisión 18: Exito, cwnd=2
    Transmisión 19: Exito, cwnd=3
    Transmisión 20: Exito, cwnd=4

![image](https://github.com/user-attachments/assets/6b3718e6-dba1-4877-ab0c-e55b55946cf5)


La simulación permite observar cómo la ventana de congestión aumenta durante transmisiones exitosas y se reinicia ante eventos de pérdida, reflejando un comportamiento básico de TCP Tahoe.
