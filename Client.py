import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 8080

client_socket.connect((host, port))

message = client_socket.recv(1024)
print(message.decode('ascii'))
client_socket.close()




