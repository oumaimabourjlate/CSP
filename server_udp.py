import socket			 

## Transfer data across UDP Sockets:

sockett = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Defining the address and port number of the socket's server interface 
address_recieving, port_recieving = '192.168.1.104', 5888

# Reserving the socket's server interface
sockett.bind((address_recieving, port_recieving))

# Receiving the data
Data, Addr = sockett.recvfrom(1024)

print("Message from a host with the following address", Addr[0], "and port", Addr[1], end=':\n')
# Decoding the recieved data in str 
print(Data.decode('utf-8'))