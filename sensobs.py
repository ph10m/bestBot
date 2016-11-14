from sensors.irproximity_sensor import IRProximitySensor as IR_sensor
from sensors.reflectance_sensors import ReflectanceSensors as Ref_sensor
from camera.camera import Camera
from camera.img import ImageMod
from sensors.ultrasonic import Ultrasonic as Echo


class IR_sensob:

    def __init__(self):
        self.sensor = IR_sensor()
        self.right = False
        self.left = False

    def update(self):
        self.sensor.update()

    def reset(self):
        self.sensor.reset()
        self.right = False
        self.left = False

    def get_value(self):
        val = self.sensor.get_value()
        if val is None:
            self.left, self.right = False, False
        else:
            self.left, self.right = val
        print (self.left, self.right)
        return [self.right, self.left]
        
class Reflectance_sensob:

    def __init__(self):
        self.sensor = Ref_sensor(False, 100, 2800)  # True = autocalibration, takes 5 seconds
        self.bool_values = [False, False, False, False, False, False]

    def update(self):
        self.sensor.update()

    def reset(self):
        self.sensor.reset()
        self.bool_values = [False, False, False, False, False, False]

    def get_value(self):
        value = self.sensor.get_value()
        print (value)
        for i in range(len(value)):
            self.bool_values[i] = value[i] < 0.85
        # print (self.bool_values)
        return self.bool_values            

'''
The camera should only operate whenever
a distance below less than 30 cm is detected
'''

class Camera_sensob:
    def __init__(self):
        self.distance = Echo()
        self.camera = Camera()
        self.imageMod = ImageMod()
        self.img = None
        self.cm = -1
        self.rec = ('None',0)
        self.counter = 0
        
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
        self.rec = ("rewind 0", 1)
        
    def update(self):
        #don't want to update the camera every update run in sensobs!
        if self.counter == 5:
            self.distance.update()
            tmp_dist = self.distance.get_value()
            print ('Dist =',tmp_dist)
            if tmp_dist > 2500 or tmp_dist is None:
                tmp_dist = 50
            # between 10 and 20, returns a higher value for lower cm
            if tmp_dist >= 10 and tmp_dist <= 20:
                priority = 1 - 0.9 * tmp_dist / 50  # halves the value and mulitplies it by 0.1
                self.react_near_wall(priority)
            elif tmp_dist < 10:
                priority = 1 - 0.9 * tmp_dist / 50  # halves the value and mulitplies it by 0.1
                self.react_too_close(priority)
            self.counter = 0
        self.counter += 1

    def take_picture(self):
        self.img = self.camera.update()
        
    def isWall(self):
        # check for colours, patterns, etc.
        self.take_picture()
        if self.img is not None:
            # convert image to one with max RGB values of each pixel
            self.imageMod.setImage(self.img)
            is_wall = self.imageMod.isWall()
            if is_wall:
                return True
        return False
            
    def reset(self):
        self.distance.reset()
        self.camera.reset()
        self.rec = ('None',0)

    def get_value(self):
        return self.rec