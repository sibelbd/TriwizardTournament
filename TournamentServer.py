import socket
import time
from random import *

HOST_RPI =  '10.104.99.110'
HOST_SERVER= '10.104.127.47'
PORT_OUT= 65432
PORT_IN= 65431
#computer generated gesture variable
cgg= 0
#0 means CPU wins 1 means player wins
winner= 0

"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_RPI,PORT_OUT))
    #Command to trigger start of gameplay
    begin= input("Prepare to battle. Press enter to start countdown.")
    begin= begin.encode()
    s.sendall(begin)

    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("Cast Your Spell!")

#may need a new method to listen
    #s.connect(HOST_SERVER,PORT_IN)
    #s.listen()
    #data = conn.recv(1024)
    #conn, addr = s.accept()
    #with conn:
     #   print('Connected by', addr)
      #  while True:
       #     print('right after while loop')
        #    data = conn.recv(1024)
         #   print(data)
          #  if not data:
           #     break
            #conn.sendall(data)"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST_SERVER,PORT_IN))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        data = data.decode()
        data = int(data)
        cgg= randint(1,3)
        if data==0:
            print("Unknown gesture, please restart program.")
        elif data==1:
            if cgg==1:
                print("tie")
            elif cgg==2:
                print("Cloak covers stone. You win.")
            elif cgg==3:
                print("Wand destroys cloak. You lose.")
        elif data==2:
            if cgg==1:
                print("Stone is covered by cloak. You lose.")
            elif cgg==2:
                print("tie")
            elif cgg==3:
                print("Stone crushes wand. You win")
        elif data==3:
            if cgg==1:
                print("Wand destroys cloak. You win.")
            elif cgg==2:
                print("Stone crushes Wand. You lose.")
            elif cgg==3:
                print("tie")



