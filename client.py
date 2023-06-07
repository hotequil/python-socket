from socket import socket, AF_INET, SOCK_STREAM
from config import host, port, buffer_size

client = socket(AF_INET, SOCK_STREAM)

client.connect((host, port))

while True:
    message = input('Input a lowercase message or "exit" (if you want to stop this socket): ')

    client.send(message.encode())

    if message == 'exit':
        client.close()
        break

    modified_message = client.recv(buffer_size)

    print(f'Response message: {modified_message.decode()}')
