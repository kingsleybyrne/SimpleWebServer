import socket,sys

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

PORT = 6789
addr = "localhost"

print("Connecting to server")
serverSocket.connect((addr,PORT))

try:
    message = "Hello NetFun this is my clientServer"
    print(sys.stderr,'Sending message: "%s"' % message)
    serverSocket.sendall(message)

    recv =0
    expected = len(message)

    while recv < expected:
        data = serverSocket.recv(16)
        recv += len(data)

finally:
    print("Closing socket")
    serverSocket.close()