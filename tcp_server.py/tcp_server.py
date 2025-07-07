import socket

# إعداد السيرفر
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))  # نفس البورت اللي فالكلينت
server_socket.listen(1)

print("[+] TCP Server listening on 127.0.0.1:9999...")

client_socket, address = server_socket.accept()
print(f"[+] Connection from {address}")

data = client_socket.recv(1024).decode()
print("Received from client:", data)

client_socket.send("Hello from TCP Server".encode())
client_socket.close()
server_socket.close()
