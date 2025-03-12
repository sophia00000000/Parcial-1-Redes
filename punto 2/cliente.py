import socket
import sys
import threading

def receive_messages(client_socket):
    try:
        while True:
            # recibir respuesta
            respuesta = client_socket.recv(1024).decode('utf-8')
            if not respuesta:
                print("Conexión cerrada por el servidor")
                break
            print(f"Respuesta del servidor: {respuesta}")
    except Exception as e:
        print(f"Error al recibir mensajes: {e}")

def start_client(nombre_cliente):
    # crear socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # conectar al servidor
        client_socket.connect(('127.0.0.1', 2010))
        print("Conectado al servidor en localhost:2010")
        
        # inicia el hilo para recibir mensajes
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()
        
        # envía el mensaje de presentación
        mensaje_inicial = f"Hola, soy el cliente {nombre_cliente}"
        print(f"Enviando mensaje: {mensaje_inicial}")
        client_socket.send(mensaje_inicial.encode('utf-8'))
        
        # bucle para enviar mensajes
        print("\nEscribe los mensajes a enviar (escribe 'salir' para terminar):")
        while True:
            mensaje = input("> ")
            if mensaje.lower() == 'salir':
                break
            client_socket.send(mensaje.encode('utf-8'))
            
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    # obtener el nombre del cliente desde los argumentos de línea de comandos
    if len(sys.argv) > 1:
        nombre_cliente = sys.argv[1]
    else:
        nombre_cliente = input("Ingresa tu nombre: ")
    
    start_client(nombre_cliente)
