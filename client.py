import socket 

# Creating a UDP socket. 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# The argument socket.SOCK_DGRAM specifies the type as a UDP socket.)
# The argument socket.AF_INET, specifies that the socket will communicate over the Internet using IPv4.
# Other option : AF_INET6 for IPv6, AF_UNIX for communication on the same machine.
# This doesn’t send any data over the network it just sets up the local data structures that will keep 
# information about this socket.


# Define the port on which you want to connect 
port = 12345			

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection 
s.close()	 
	
'''