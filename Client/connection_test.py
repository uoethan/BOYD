import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 12345))
clientsocket.send(b'hello')
print(clientsocket.recv(1024).decode())

clientsocket.close()