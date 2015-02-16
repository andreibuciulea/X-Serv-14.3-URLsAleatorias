#!/usr/bin/python

import socket
import random
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((socket.gethostname(), 1235))

mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections'
        usuario = socket.gethostname()
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        aleatorio = str(int(random.random() * 1000000))
        recvSocket.send("HTTP/1.1 404 Not Found\r\n\r\n" +
                        "<html><body><h1>Hello World!</h1>" +
                        "<h2>Schools</h2>" +
                        "<a href= http://" + usuario + ":1235/" + aleatorio +
                        ">Dame otra</a>" +
                        " <img src='http://www.w3schools.com/images/" +
                        "w3schools_green.jpg'> " +
                        "<p>And in particular hello to you, " +
                        str(address[0]) + "</p>" + "</body></html>" +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
