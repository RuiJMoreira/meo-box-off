import socket
HOST = "192.168.1.67"
PORT = 8082
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b"key=151\n")
s.close()
