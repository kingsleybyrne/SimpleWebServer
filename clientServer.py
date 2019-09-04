import socket,sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 6789
addr = "localhost"
serverSocket.bind((addr,PORT))
serverSocket.listen(1)

while True:
    print("Waiting for connection")
    connection, clientAddr = serverSocket.accept()
    try:
        print("Connection from ",clientAddr)
        while True:
            data = connection.recv(16)
            print(sys.stderr, 'recieved "%s"' % data)
            if data:
                print("Sending data back to client")
                connection.sendall(data)
            else:
                print("No more data")
                break
    finally:
        connection.close()