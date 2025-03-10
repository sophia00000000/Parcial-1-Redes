import socket
import sys

def start_client(nombre_cliente):
    # crear socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # conectar al servidor
        client_socket.connect(('127.0.0.1', 2010))
        print("Conectado al servidor en localhost:2010")
        
        mensaje = f"Hola, soy el cliente {nombre_cliente}"
        print(f"Enviando mensaje: {mensaje}")
        client_socket.send(mensaje.encode('utf-8'))
        
        # recibir respuesta
        respuesta = client_socket.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {respuesta}")
        
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    # obtener el nombre del cliente
    if len(sys.argv) > 1:
        nombre_cliente = sys.argv[1]
    else:
        nombre_cliente = input("Ingresa tu nombre: ")
    
    start_client(nombre_cliente)
