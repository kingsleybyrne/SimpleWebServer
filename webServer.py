import socket
from socket import *
import selectors
import sys
import http.server
import socketserver

serverSocket = socket(AF_INET, SOCK_STREAM)
PORT = 6789
print("Hostname is ",gethostname())
serverSocket.bind(("localhost",PORT))
# Bind the port number to localhost connection

selector = selectors.DefaultSelector()
serverSocket.listen(5)
# Listen to this many connections

# print("Listening on ", (getaddrinfo()))
# serverSocket.setblocking(False)
# selector.register(serverSocket, selectors.EVENT_READ, data=None)

# def accept_wrapper(sock):
#     conn,addr=sock.accept
#     print("Accepted connection from",addr)
#     conn.setBlocking(False)
#     data = types.SimpleNamespace(addr=addr,inb=b'',outb=b'')
#     events=selectors.EVENT_READ | selectors.EVENT_WRITE
#     selector.register(conn,events,data=data)


while True:
    # Infinite loop -- needed to accept all connections and not go out unless socket closed
    # events= selector.select(timeout=None)
    # for key, mask in events:
    #     if key.data is None:
    #         accept_wrapper(key.fileObj)
    #     else:
    #         service_Connection(key,mask)
        print("Ready to serve")
        connectionSocket, addr = serverSocket.accept()
        # accepts the incoming connection
        try:
            # Part of the exception handling (Try-Catch in java)
            message = connectionSocket.recv(1024)
            print(":",message)
            fileName = message.split()[1]
            # fileName = "C:\users\kings\Desktop\UTS Degree\Subjects\Web Systems\WebSystemsProject\index.html"
            f = open(fileName[1:])
            print("Filename:",fileName)
            outputData = f.read()
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

            for i in range(0,len(outputData)):
                # For loop running through the input message then sends to browser
                connectionSocket.send(outputData[1])
                connectionSocket.send("\r\n")

            connectionSocket.close()
        except IOError:
            # Exception handling is thrown if it cant find the file the messsage attribute is looking for
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
            connectionSocket.close()

serverSocket.close()
# Close the socket -- Must always do to stop a memory leak
