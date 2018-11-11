import logging
import sys
import time
import numpy as np

from Adafruit_BNO055 import BNO055


# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
#bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)
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
    
gesture = 1

num_trials = 40
duration = 1.2
num_samples = int(duration * 100)
features = 6

data = np.empty([num_trials,features*num_samples])

counter = 0

for trial in range(num_trials):
	start = input('Trial %d. Press any key to continue.' %trial)
	features = []
	
	for sample in range(num_samples):
		features += get_data()
		time.sleep(0.01)
	
	row = np.array(features)
	
	data[trial,:] = row

num_labels = int(num_trials/4)
labels = [1] * num_labels + [2] * num_labels + [3] * num_labels + [0] * num_labels
labels = np.array(labels)



np.savetxt('labels.txt',labels)
np.savetxt('data.txt',data)
print(data.shape)
print(labels.shape)



		
