import socket

## Transfer data across TCP Sockets:
 
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('192.168.1.104', 4001))
soc.connect(('192.168.1.104', 4000))

soc.send(b'blablabla')
# We use the function send() with one argument than the function sendto() with two arguments

# To close the connection
soc.shutdown(socket.SHUT_RDWR)