class Motob:
    def __init__(self):
        # definer funksjoner for alle sensorene i en dict
        # self.sensors = {
            # Camera:             self.react_camera,
            # IRProximitySensor:  self.react_IR,
            # ReflectanceSensors: self.react_reflect,
            # Ultrasonic:         self.react_ultra
        # }
        self.value = 0

	def update(self, recommendation):
		self.value = recommendation
		self.operate(recommendation)
		
	def operate(recommended):
		pass

    # def run(sensor, value):
        # # tar inn en tuppel med sensor, verdi
        # '''
        # feks:
        # kamera ser at et objekt dekker nesten hele field-of-view (objektet er nært)
        # får da inn en høy verdi i tuppelen, og må feks rygge lengre bak, enn om objektet hadde vært lengre unna
        # '''
        # sensor = sensor.__class__.__name__
        # print ('Motor controller received the highest priority from',sensor,'with a value of',value)
        
        # # ...finnes sensoren?
        # if sensor in self.sensors:
            # # kjører funksjonen definert i self.sensors-dict
            # self.sensors[name]()
            # current_value = value
        
    # # definer hvordan motoren skal reagere for hver type sensor - bruk self.value
    # def react_camera(self):
        # pass
        
    # def react_IR(self):
        # pass
        
    # def react_reflect(self):
        # pass
        
    # def react_ultra(self):
        # pass

