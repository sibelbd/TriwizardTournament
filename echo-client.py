import socket

HOST = '10.104.127.47'
PORT = 65431

text = 'start'
cookies = text.encode()
print(cookies)








with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	print('Connected to host')
	s.sendall(cookies)
	print('Data sent')
	data = s.recv(1024)
	
print('Received', repr(data))
