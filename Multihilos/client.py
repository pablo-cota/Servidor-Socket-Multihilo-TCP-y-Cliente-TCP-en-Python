import socket

#
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "adios"

#Protocolo de conexión
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[Conectado] El cliente se conectado al servidor por {IP}:{PORT}")


    #Parte encargada de la mensajeria 
    connected = True
    while connected:
        msg = input("> ")

        client.send(msg.encode(FORMAT))

        #Continua mandando mensajes hasta que se envia la palabra indicada para la desconexión
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
    

if __name__ == "__main__":
    main()
