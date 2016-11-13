from sensobs import IR_sensob, Reflectance_sensob, Camera_sensob

class Follow_line:

    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensor = Reflectance_sensob()
        self.active_flag = False
        
    def get_sensob(self):
        return self.sensor

    def update(self):
        value = self.sensor.get_value()
        self.bbcon.recommendations.append(value)

class Avoid_collision:

    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensor = IR_sensob()
        self.active_flag = False

    def get_sensob(self):
        return self.sensor

    def update(self):
        value = self.sensor.get_value()
        print('IR Side:',value)
        bbcon.recommendations.append(value)

class Avoid_walls:

    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensor = Camera_sensob()
        self.active_flag = False

    def get_sensob(self):
        return self.sensor

        
    def update(self):
        value = self.sensor.get_value()
        bbcon.recommendations.append(value)
