import socket

HOST = '0.0.0.0'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[+] Listening on port {PORT}...")

while True:
    client, addr = server.accept()
    print(f"[+] Connection from {addr}")
    data = client.recv(1024).decode('utf-8')
    print(f"[DATA] {data}")
    client.close()