from irproximity_sensor.py import IRProximitySensor as Sensor

class IR_sensob:

    def __init__(self):
        self.sensor = Sensor()
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
        return recommendation

    def recommend(self):
    	if right and not left:
    		recommendation = ["left", 0.5]
    	elif left and not right:
    		recommendation = ["right", 0.5]
    	else:
    		recommendation = ["None", 0]