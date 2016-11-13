from sensobs import IR_sensob, Reflectance_sensob, Camera_sensob

class Follow_line:

    def __init__(self, bbcon):
        print ('Creating a follow line behavior')
        self.bbcon = bbcon
        self.sensor = Reflectance_sensob()
        self.active_flag = False
        
    def get_sensob(self):
        return self.sensor

    def update(self):
        value = self.sensor.get_value()
        self.bbcon.add_rec(value)

class Avoid_collision:

    def __init__(self, bbcon):
        print ('Creating an avoidance behavior')
        self.bbcon = bbcon
        self.sensor = IR_sensob()
        self.active_flag = False

    def get_sensob(self):
        return self.sensor

    def update(self):
        value = self.sensor.get_value()
        print('IR Side:',value)
        self.bbcon.add_rec(value)

class Avoid_walls:

    def __init__(self, bbcon):
        print ('Adding a wall-detector behavior')
        self.bbcon = bbcon
        self.sensor = Camera_sensob()
        self.active_flag = False
        self.counter = 0

    def get_sensob(self):
        return self.sensor
        
    def update(self):
        self.counter += 1
        if self.counter == 10:
            value = self.sensor.get_value()
            self.counter = 0
            self.bbcon.add_rec(value)
