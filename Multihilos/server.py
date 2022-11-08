import socket
import threading

#Asignación de puerto, dirección y datos generales
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "adios" #Palabra para terminar conexión

#Parte encargada de estabelcer la conexión e informa estado de conexión
def handle_client(conn, addr):
    print(f"[Nueva Conexión] {addr} conectado.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
        # msg = f"Msg received: {msg}"
        conn.send(msg.encode(FORMAT))

    conn.close()

#Especificación de protocolo de conexión y conexiones
def main():
    print("[Iniciando] El servidor esta iniciando...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] El servidor está escuchando {IP}:{PORT}")

    #Ciclo de la conversación, infinito hasta mandar la clave de desconexión
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Conexiones activas] {threading.activeCount() - 1}")


if __name__ == "__main__":
    main()
