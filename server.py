import socket

def Main():
    host = '10.42.0.1'
    port = 6666
    TestServer = socket.socket()
    TestServer.bind((host,port))
    print ("Server started!")

    TestServer.listen(1)
    c, addr = TestServer.accept()
    print ("Connection from: " + str(addr))
    while True:
        data = str(c.recv(1024))
        if not data:
            break
        print ("from connected user: " + data)
    c.close()

if __name__== '__main__':
    Main()