"""
    Random URL generator App

    Using class scheme, make a random URL generator App that imports webApp class
    provided by module webapp.py
    Usage: http://<hostname>:1234/<random-string>

Author: Ainhoa Garcia-Ruiz Fuentes
Course: Servicios y Aplicaciones en Redes de Ordenadores.

"""
import random
import socket

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        number = random.randint(0, 1e7)
        link = '<a href="http://' + str(socket.gethostname()) + ':1234/' + str(number) + '">'
        print('Answering back...')
        recvSocket.send(b'HTTP/1.1 200 OK\r\n\r\n' +
                        b'<html><body><h1>Hola, </h1>' + bytes(link, 'utf-8') +
                        b'Dame otra</a>' +
                        b'</body></html>' +
                        b'\r\n')
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
mySocket.close()
