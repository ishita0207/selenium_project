import socket
import os
from _thread import *
import random
import time

ServerSideSocket = socket.socket()
#host = '127.0.0.1'
host = '0.0.0.0'
port = 2001
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    x = random.randint(50,999)
    y = random.randint(50,999)
    connection.send(str.encode(f'Server is working, now add: {x}, {y}'))
    startTime = time.time()
    while True:
        data = connection.recv(2048)
        receivedTime = time.time()
        if receivedTime-startTime<4:
            if not data:
                break
            val = data.decode('utf-8')
            print(val,len(val))
            if len(val)>1:
                if (x+y) == int(val):
                    connection.sendall(bytes('Congrats! flag is: TFYTN2xtc3U4','utf-8'))
                else:
                    connection.sendall(bytes('Wrong','utf-8'))
            else:
                connection.send(bytes('Reject','utf-8'))
        else:
            connection.send(bytes('Too Slow. Try Again!','utf-8'))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()