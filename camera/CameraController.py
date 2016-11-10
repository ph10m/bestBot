from camera.camera import Camera
from camera.img import ImageMod
from sensors.ultrasonic import Ultrasonic as Sensor

'''
The camera should only operate whenever
a distance below less than 30 cm is detected
'''

class CameraOb:
	def __init__(self):
		self.distance = Sensor()
		self.camera = Camera()
		self.imageMod = ImageMod()
		self.img = None
		self.cm = -1
		
	def update(self):
		self.distance.update()
		#don't want to update the camera at any time!
		
	def take_picture(self):
		self.img = self.camera.update()
		
	def analyze_picture(self):
		# check for colours, patterns, etc.
		pass
	
	def reset(self):
		self.distance.reset()
		self.camera.reset()

	def get_value(self):
		# simply get the distance in cm
		self.cm = self.distance.get_value()
		return self.cm

	def recommend(self):
		# based on either distance or camera,
		# create a recommendation
		pass