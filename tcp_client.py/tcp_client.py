import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))
client_socket.send(b"Hello from TCP Client")
data = client_socket.recv(1024)
print("Received from server:", data.decode())
client_socket.close()
