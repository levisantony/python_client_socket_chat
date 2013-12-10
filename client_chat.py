#client code

from socket import *            
 
host="127.0.0.1"        	# Address of the server :: 127.0.0.1 equivalent to "localhost"
port=5555               	# Assign a specific port for your application
 
s=socket(AF_INET, SOCK_STREAM)  # Creates a socket
s.connect((host,port))          # Connecting to server
msg=s.recv(1024)            	# Receive data from server (1024 bytes)
print "Server : " + msg

s.close()
