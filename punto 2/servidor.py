import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Conexión aceptada desde {client_address[0]}")
    nombre_cliente = "Desconocido"
    
    try:
        connected = True
        while connected:
            # recibe mensaje del cliente
            mensaje = client_socket.recv(1024).decode('utf-8')
            
            if not mensaje:
                # si el mensaje está vacío, desconectar al cliente
                connected = False
                continue
                
            print(f"Mensaje recibido: {mensaje}")
            
            # extraer el nombre del cliente del primer mensaje
            if "Hola, soy el cliente" in mensaje and nombre_cliente == "Desconocido":
                nombre_cliente = mensaje.split("cliente ")[1]
                respuesta = f"Mensaje recibido de {nombre_cliente}"
            else:
                respuesta = f"Mensaje recibido de {nombre_cliente}: '{mensaje}'"
            
            # enviar la respuesta
            client_socket.send(respuesta.encode('utf-8'))
            print(f"Respuesta enviada: {respuesta}")
            
    except Exception as e:
        print(f"Error al comunicarse con el cliente: {e}")
    finally:
        # cerrar la conexión cuando se interrumpe la comunicación
        client_socket.close()
        print(f"Conexión con {client_address[0]} ({nombre_cliente}) cerrada")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # permite reutilizar la dirección
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # enlaza a la dirección y puerto
    server_socket.bind(('127.0.0.1', 2010))
    
    # escuchar conexiones (máximo 5)
    server_socket.listen(5)
    
    print("Servidor escuchando en el puerto 2010...")
    
    try:
        while True:
            # aceptar conexiones entrantes
            client_socket, client_address = server_socket.accept()
            
            # crear un nuevo hilo para manejar al cliente
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario") # ctrl+c
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
