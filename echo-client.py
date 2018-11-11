import socket

HOST = '10.104.127.47'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	print('Connected to host')
	s.sendall(b'Hello,world')
	print('Data sent')
	data = s.recv(1024)
	
print('Received', repr(data))
