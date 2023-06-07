from socket import socket, AF_INET, SOCK_DGRAM
from config import host, port, buffer_size

client = socket(AF_INET, SOCK_DGRAM)
message = input('Input a lowercase message: ')

client.sendto(message.encode(), (host, port))

modifiedMessage, address = client.recvfrom(buffer_size)

print(f"Response message: {modifiedMessage.decode()}")
print(f"Server: {address}")

client.close()
