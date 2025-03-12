import random
cwnd = 1
import matplotlib.pyplot as plt


# arreglos para graficar
arrTransmisiones = []
arrCwnd = []

# Simulación de TCP s
for i in range(20):
    exito = random.randint(1, 100) <= 80  # Probabilidad de éxito 80%
 
    if exito:
        cwnd += 1
    else:  # Pprdida de paquete
        cwnd = 1  # Reiniciar cwnd
    print(f"Transmisión {i + 1}: {'Exito' if (exito)else 'Pérdida'}, cwnd={cwnd}"
          
    arrTransmisiones.append(i + 1)
    arrCwnd.append(cwnd)

# Graficar resultados 
plt.figure(figsize=(10, 5))
plt.plot(arrTransmisiones, arrCwnd, marker='o', linestyle='-', label="Ventana de Congestión (cwnd)", color="blue")


plt.xlabel("Número de Transmisión")
plt.ylabel("Tamaño de Ventana de Congestión (cwnd)")
plt.title("Simulación TCP Tahoe")
plt.legend()
plt.grid()
plt.show()
