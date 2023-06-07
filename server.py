from socket import socket, AF_INET, SOCK_STREAM
from config import port, buffer_size

server = socket(AF_INET, SOCK_STREAM)

server.bind(('', port))

print('Server is running!')

server.listen(1)
connection, address = server.accept()

print(f'Address: {address}')

while True:
    message = connection.recv(buffer_size).decode()

    if message == 'exit':
        connection.close()
        break

    print(f'Received message: {message}')

    connection.send(message.upper().encode())
