import socket

HOST_RPI = '10.104.99.110'
HOST_SERVER = '10.104.127.47'
PORT = 65431


# listening for gameplay start
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST_RPI,PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by',addr)
		while True:
			print('Checking input')
			data = conn.recv(1024)
			print(data)
			if data is "b'start'":
				#play game
				print('playing game')
			else:
				print('empty')
				break
		
		

# countdown

# spell casting

# predicting

# send label






#with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
#	c.connect((HOST,PORT))
#	print('Connected to host')
#	c.sendall(cookies)
#	print('Data sent')
#	data = c.recv(1024)
	
#print('Received', repr(data))
