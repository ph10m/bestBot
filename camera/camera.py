import os
from PIL import Image

class Camera():
	def __init__(self, img_width=128, img_height=96, img_rot=0):
		self.img = None
		self.img_width = img_width
		self.img_height = img_height
		self.img_rot = img_rot
		print ('Camera initialized!')

	def get_img(self):
		return self.img

	def update(self):
		print ('Fetching a new image...')
		self.sensor_get_img()
		return self.img
		
	def reset(self):
		self.img = None

	def sensor_get_img(self):
		# This is a OS call that takes a image and makes it accessible to PIL operations in the same directory
		os.system('raspistill -t 1 -o image.png -w "' + str(self.img_width) + '" -h "' + str(self.img_height) + '" -rot "' + str(self.img_rot) + '"')
		# Open the image just taken by raspicam
		# Stores the RGB array in the img field
		self.img = Image.open('image.png').convert('RGB')

# Just testing the camera in python

# os.system('raspistill -t 1 -o image.png -w "' + str(200) + '" -h "' + str(200) + '" -rot "' + str(0) + '"')