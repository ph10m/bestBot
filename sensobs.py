from sensors.irproximity_sensor import IRProximitySensor as IR_sensor
from sensors.reflectance_sensors import ReflectanceSensors as Ref_sensor
from camera.camera import Camera
from camera.img import ImageMod
from sensors.ultrasonic import Ultrasonic as Echo


class IR_sensob:

    def __init__(self):
        self.sensor = IR_sensor()
        self.value = None
        self.right = False
        self.left = False
        self.recommendation = []

    def update(self):
        self.sensor.update()

    def reset(self):
        self.sensor.reset()
        self.value = None
        self.right = False
        self.left = False

    def get_value(self):
        self.value = self.sensor.get_value()
        self.right = value[0]
        self.left = value[1]
        recommend()
        return self.recommendation

    def recommend(self):
        if right and not left:
            self.recommendation = ["left 45", 0.5]
        elif left and not right:
            self.recommendation = ["right 45", 0.5]
        else:
            self.recommendation = ["None", 0]

class Reflectance_sensob:

    def __init__(self):
        self.sensor = Ref_sensor(True)  # True = autocalibration, takes 5 seconds
        self.bool_values = [False, False, False, False, False, False]
        self.recommendation = []

    def update(self):
        self.sensor.update()

    def reset(self):
        self.sensor.reset()
        self.bool_values = [False, False, False, False, False, False]
        self.recommendation = []

    def get_value(self):
        value = sensor.get_value()
        for i in range(len(value)):
            bool_values[i] = value[i] > 0.85
        return recommend()

    def recommend(self):
        if self.bool_values[0]:
            return ["left 60", 1]
        elif self.bool_values[5]:
            return ["right 60", 1]
        elif self.bool_values[1]:
            return ["left 30", 0.75]
        elif self.bool_values[4]:
            return ["right 30", 0.75]
        else:
            return ["None", 0]

            

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