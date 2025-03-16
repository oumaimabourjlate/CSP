import socket

## Transfer data across TCP Sockets:

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('192.168.1.104', 4000))
sock.listen()

socket0, conn_address = sock.accept()

data = socket0.recv(1024)

# We use the function recv() instead of recvfrom()
print(data.decode('utf-8'))

# To close the connection
socket0.shutdown(socket.SHUT_RDWR)

# To close the listening socket
sock.close()