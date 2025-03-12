# Punto 2: Simulación de Conexión de Sockets en Python

## Enunciado

Se solicita desarrollar un programa en **Python** que simule la conexión de varios clientes a un servidor local utilizando sockets **TCP**. El servidor debe ejecutarse en el puerto **2010** y aceptar conexiones de múltiples clientes. Cada cliente debe enviar un mensaje al servidor indicando su nombre y el servidor debe responder confirmando la recepción del mensaje.

### Servidor

- Escucha en el puerto 2010
- Acepta múltiples conexiones mediante hilos (threading)
- Cuando recibe un mensaje, extrae el nombre del cliente
- Envía una confirmación con el formato especificado

![image](https://github.com/user-attachments/assets/f98b09ca-3a80-4592-bb04-a87a55e93bf2)


### Clientes

 - Se conecta al servidor en localhost:2010
- Envía un mensaje con su nombre en el formato solicitado
- Recibe y muestra la respuesta del servidor
- Permite especificar el nombre del cliente mediante argumentos de línea de comandos
- Mantiene la conexión abierta para enviar y recibir más mensajes además del predeterminado

![image](https://github.com/user-attachments/assets/7f87c321-3824-4d4d-9962-fd1dd8fe2316)

![image](https://github.com/user-attachments/assets/101b5373-f769-49c1-9ce7-45b746a24932)

![image](https://github.com/user-attachments/assets/7ca3d0c1-bba5-4dfa-9a77-d8585413197b)

![image](https://github.com/user-attachments/assets/d5cc2163-26f0-4fc3-9c75-c6086252554f)








