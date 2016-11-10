from camera.camera import Camera
from camera.img import ImageMod
from sensors.ultrasonic import Ultrasonic as Sensor

'''
The camera should only operate whenever
a distance below less than 30 cm is detected
'''

class Camera_sensob:
	def __init__(self):
		self.distance = Sensor()
		self.camera = Camera()
		self.imageMod = ImageMod()
		self.img = None
		self.cm = -1
        self.rec = ('None',0)
		
    def react_near_wall(self, priority):
        print ('I see something 10-20 cm away!')
        # turn around 180 degrees
        if self.isWall():
            self.rec = ("right 180", priority)
        else:
            self.rec = ("random 90", priority)
        
    def react_too_close(self, priority):
        print ('I see something right in front!')
        # reverse for a bit and turn 90 degrees randomly
        self.rec = ("rewind", priority)
        
	def update(self):
        tmp_dist = self.distance.update()
        # between 10 and 20, returns a higher value for lower cm
		if tmp_dist => 10 and tmp_dist <= 20:
            priority = 1 - 0.9 * tmp_dist / 50  # halves the value and mulitplies it by 0.1
            self.react_near_wall(priority)
        elif tmp_dist < 10:
            priority = 1 - 0.9 * tmp_dist / 50  # halves the value and mulitplies it by 0.1
            self.react_too_close()
		#don't want to update the camera every update run in sensobs!
		
	def take_picture(self):
		self.img = self.camera.update()
        
	def isWall(self):
		# check for colours, patterns, etc.
		if self.img is not None:
            # convert image to one with max RGB values of each pixel
            is_wall = self.imageMod.checkWall()
            if self.imageMod.isWall():
                return True
        return False
            
	def reset(self):
		self.distance.reset()
		self.camera.reset()
        self.rec = ('None',0)

	def get_value(self):
		return self.rec