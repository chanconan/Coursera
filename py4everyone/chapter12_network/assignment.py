import socket
# socket.SOCK_STREAM essentially creates an endpoint on machine to be connected, but has yet to be connected. 
# connection point that has yet to be connected
# connect() connects the socket object to the host and the port
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysocket.close()