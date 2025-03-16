# Client-Sever Program

### Since working within a SDN envirement is calling for previous knowledge on Socket's programming, I decided to start my firt project on this path.

### This mini project is a simple program to facilitate communication between a client and a server in Python. After finshing this mini project, I'll try to create another version in c++.

## Let's GO! :)

### This an image from the book *Data and Computer Communications - William Stallings*.

![D](DCC.png "Data and Computer Communication")


### When the APPY of the Host A wants to send data to the APPY of the other Host B, the data will be transferred through the layers of the TCP/IP model because the Hosts are in different networks.  However, the details of the procedure are hidden from the the application layer. APPYs can directly send and receive data across the logical connection => the socket API! => a programming interface that connects the application layer to the transport layer and from there, the rest of the TCP/IP protocol stack.

## UDP Socket:

* ### Sending Data : 
1. Create a UDP socket.
2. (Optional) Bind to the local IP address and UDP port that the socket should use. 
(If you don’t choose a port, the operating system will select a random large port number for you when you first try to send data.)
3. Send data, by specifying the data to send and the destination IP address and port.

* ### Receiving Data : 

1. Create a UDP socket.
2. Bind to the local IP address and UDP port that the socket should use.
3. Receive data from the socket buffer, where the operating system will have put any data that was passed up the network protocol stack for this UDP port.


## TCP Socket:

### Later :)
