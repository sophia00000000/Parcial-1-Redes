import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Conexión aceptada desde {client_address[0]}")
    
    try:
        # recibe mensaje del cliente
        mensaje = client_socket.recv(1024).decode('utf-8')
        print(f"Mensaje recibido: {mensaje}")
        
        # obtiene el nombre del cliente
        if "Hola, soy el cliente" in mensaje:
            nombre_cliente = mensaje.split("cliente ")[1]
        else:
            nombre_cliente = "Desconocido"
        
        # envía respuesta
        respuesta = f"Mensaje recibido de {nombre_cliente}"
        client_socket.send(respuesta.encode('utf-8'))
        print(f"Respuesta enviada: {respuesta}")
        
    except Exception as e:
        print(f"Error al comunicarse con el cliente: {e}")
    finally:
        # cierra la conexión
        client_socket.close()
        print(f"Conexión con {client_address[0]} cerrada")

def start_server():
    """
    Inicia el servidor y escucha conexiones entrantes
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 2010))
    # escucha conexiones (máximo 5)
    server_socket.listen(5)
    
    print("Servidor escuchando en el puerto 2010...")
    
    try:
        while True:
            # acepta conexiones entrantes
            client_socket, client_address = server_socket.accept()
            
            # crea un nuevo hilo para manejar al cliente
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
