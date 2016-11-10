from reflectance_sensors.py import ReflectanceSensors as Sensor

class Reflectance_sensob:

    def __init__(self):
        self.sensor = Sensor(True) 	# True = autocalibration, takes 5 seconds
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

