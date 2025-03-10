# Punto 2: Simulación de Conexión de Sockets en Python

## Enunciado

Se solicita desarrollar un programa en **Python** que simule la conexión de varios clientes a un servidor local utilizando sockets **TCP**. El servidor debe ejecutarse en el puerto **2010** y aceptar conexiones de múltiples clientes. Cada cliente debe enviar un mensaje al servidor indicando su nombre y el servidor debe responder confirmando la recepción del mensaje.

### Servidor

- Escucha en el puerto 2010
- Acepta múltiples conexiones mediante hilos (threading)
- Cuando recibe un mensaje, extrae el nombre del cliente
- Envía una confirmación con el formato especificado

### Cliente

 - Se conecta al servidor en localhost:2010
- Envía un mensaje con su nombre en el formato solicitado
- Recibe y muestra la respuesta del servidor
- Permite especificar el nombre del cliente mediante argumentos de línea de comandos

## Evidencias de ejecución

![image](https://github.com/user-attachments/assets/78afd0fb-dcfb-4034-b3de-f615fd8d3bea)

![image](https://github.com/user-attachments/assets/ea72f462-c1b0-4649-be8e-c6992e305759)

![image](https://github.com/user-attachments/assets/d51b92a5-ea98-4a13-8ae2-e5bd0f83f0af)

![image](https://github.com/user-attachments/assets/f3e69a2b-0dc0-4434-be9e-a0eeb4151798)

![image](https://github.com/user-attachments/assets/b4ec76a2-524f-4910-8221-45227e92a7ad)






