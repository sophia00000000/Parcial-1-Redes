# Punto 3: Comportamiento de TCP ante Congestión de Red

Simulación en Python para representa el comportamiento de la ventana de congestión (cwnd) de TCP en función de eventos simulados de éxito o pérdida de paquetes.

- Inicialmente, la ventana de congestión (cwnd) tiene un valor de 1.
- Por cada transmisión exitosa (simulada), el valor de la ventana debe incrementarse en uno.<code> cwnd += 1 </code>
- Si ocurre una pérdida de paquete, la ventana de congestión debe reducirse drásticamente (similar a un reinicio a la fase de Slow Start). <code> cwnd = 1 </code>

Simulación de 20 transmisiones, donde cada transmisión puede tener éxito (probabilidad del 80%) o fallar (probabilidad del 20%).

    exito = random.randint(1, 100) <= 80 

  
---
### Salida 

    Transmisión 1: Exito, cwnd=1
    Transmisión 2: Exito, cwnd=2
    Transmisión 3: Exito, cwnd=3
    Transmisión 4: Exito, cwnd=4
    Transmisión 5: Exito, cwnd=5
    Transmisión 6: Exito, cwnd=6
    Transmisión 7: Exito, cwnd=7
    Transmisión 8: Exito, cwnd=8
    Transmisión 9: Exito, cwnd=9
    Transmisión 10: Pérdida, cwnd=1      
    Transmisión 11: Exito, cwnd=2        
    Transmisión 12: Exito, cwnd=3        
    Transmisión 13: Exito, cwnd=4        
    Transmisión 14: Exito, cwnd=5        
    Transmisión 15: Exito, cwnd=6        
    Transmisión 16: Pérdida, cwnd=1      
    Transmisión 17: Exito, cwnd=2        
    Transmisión 18: Pérdida, cwnd=1      
    Transmisión 19: Exito, cwnd=2        
    Transmisión 20: Exito, cwnd=3 

![image](https://github.com/user-attachments/assets/7fe6e7b0-2224-41a8-a482-65c2c3ad0b38)



La simulación permite observar cómo la ventana de congestión aumenta durante transmisiones exitosas y se reinicia ante eventos de pérdida, reflejando un comportamiento básico de TCP Tahoe.
