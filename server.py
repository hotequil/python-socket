from socket import socket, AF_INET, SOCK_DGRAM
from config import port, buffer_size

server = socket(AF_INET, SOCK_DGRAM)

server.bind(('', port))

print('Server is running!')

while True:
    message, address = server.recvfrom(buffer_size)
    modifiedMessage = message.upper()

    server.sendto(modifiedMessage, address)
