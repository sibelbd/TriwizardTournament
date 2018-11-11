import socket
import logging
import sys
import time
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from Adafruit_BNO055 import BNO055

HOST_RPI = '10.104.99.110'
HOST_SERVER = '10.104.127.47'
PORT_OUT = 65431
PORT_IN = 65432

def record_spell():

	bno = BNO055.BNO055()

	def get_data():
		
		x,y,z = bno.read_euler()
		a,b,c = bno.read_gyroscope()
		
		return [x,y,z,a,b,c]


	# Enable verbose debug logging if -v is passed as a parameter.
	if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
		logging.basicConfig(level=logging.DEBUG)

	# Initialize the BNO055 and stop if something went wrong.
	if not bno.begin():
		raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')
		
	num_trials = 1
	duration = 1.2
	num_samples = int(duration * 100)
	features = 6

	data = np.empty([num_trials,features*num_samples])

	for trial in range(num_trials):
		features = []
		
		for sample in range(num_samples):
			features += get_data()
			time.sleep(0.01)
		
		row = np.array(features)
		
		data[trial,:] = row
		
	return data

model = None
data = np.loadtxt('data.txt')
label = np.loadtxt('labels.txt')
model = KNeighborsClassifier(n_neighbors=1)
model = model.fit(data,label)
	
def play():
	
	#countdown
	print('countdown')
	for i in range(3):
		print(3-i)
		time.sleep(1)
	
	#record spell
	print('recording spell')
	spell = record_spell()
	print(spell)
	print(spell.shape)
	
	#predict
	print('predicting gesture')
	gesture = model.predict(spell)
	gesture = gesture[0]
	print(gesture)
	
	#send label
	print('sending label')
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
		c.connect((HOST_SERVER,PORT_OUT))
		print('Connected to host')
		gesture = str(int(gesture))
		gesture = gesture.encode()
		c.sendall(gesture)
		print('Data sent')


#instructions
print("Welcome to the Triwizard Tournament")
print("Please prepare to do one of three gestures")
print("1) Counterclockwise circle = Cloak")
print("2) Up and down motion = Stone")
print("3) Center to right then left = Wand")
print("Cloak covers Stone, Stone crushes Wand, Wand destroys Cloak")




# listening for gameplay start
"""with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST_RPI,PORT_IN))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by',addr)
			
		data = conn.recv(1024)
			
		print('Packet received')"""
play()
		









		
		
		
		
		





