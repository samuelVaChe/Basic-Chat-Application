import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 8080
msg=open("message.txt")

try:
    server_socket.bind((host, port))
except socket.error as e:
    if e.errno == 98:
        print(f"Port {port} is already in use. Please choose a different port.")
        exit()
    else:
        raise

server_socket.listen(5)
print("Server listening for client {}:{}".format(host, port))

while True:
    client_socket, address = server_socket.accept()
    print('Got connection from', address)

    message = msg.read()
    client_socket.send(message.encode('ascii'))

    client_socket.close()




