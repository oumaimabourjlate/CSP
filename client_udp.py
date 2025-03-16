import socket 

## Transfer data across UDP Sockets:

# Creating the socket object
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# The argument socket.SOCK_DGRAM specifies the type as a UDP socket.)
# The argument socket.AF_INET, specifies that the socket will communicate over the Internet using IPv4.
# Other option : AF_INET6 for IPv6, AF_UNIX for communication on the same machine.
# This doesn’t send any data over the network it just sets up the local data structures that will keep 
# information about this socket.

# Opening the text and reading it in binary mode (rb)
with open('texte.md', "rb") as file:
    data = file.read()
# data is already in bytes format

# (Optional) Defining the address and port number of the socket's client interface 
address_recieving , port_recieving  = '192.168.1.104', 5889
# (Optional) Reserving the socket's client interface or the os will shoose a random port
socket1.bind((address_recieving, port_recieving))

# Defining the address and port number of the socket's server interface 
address_sending, port_sending = '192.168.1.104', 5888

# Sending the data
socket1.sendto(b'data', (address_sending, port_sending))
