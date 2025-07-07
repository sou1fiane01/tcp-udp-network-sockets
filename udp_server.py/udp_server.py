import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8888))
print("UDP Server is running...")

data, addr = server_socket.recvfrom(1024)
print("Received:", data.decode())
server_socket.sendto(b"Hello from UDP Server", addr)
