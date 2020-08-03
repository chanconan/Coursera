import socket
# socket.SOCK_STREAM essentially creates an endpoint on machine to be connected, but has yet to be connected. 
# connection point that has yet to be connected
# connect() connects the socket object to the host and the port
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect()