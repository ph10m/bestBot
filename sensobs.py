from irproximity_sensor.py import IRProximitySensor as IR_sensor
from reflectance_sensors.py import ReflectanceSensors as Ref_sensor

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
        update()
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
        update()
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

