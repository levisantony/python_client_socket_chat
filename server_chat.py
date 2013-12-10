# Server Code

from socket import *            
 
host="127.0.0.1"                # Address of the server :: 127.0.0.1 equivalent to "localhost"
port=5555                       # Assign a specific port for your application
 
s=socket(AF_INET, SOCK_STREAM)  # Creates a socket
s.bind((host,port))             # Bind socket
s.listen(1)                     # Socket listening for client :: 1 is the queue size
print "Waiting for connections "
q,addr=s.accept()               # Accepts request from client ::This function returns socket and address 
q.send("test message Hmicro")   # Sends data to client


s.close()
