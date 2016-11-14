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
        bool_values = self.sensor.get_value()
        recommended = self.recommend(bool_values)
        self.bbcon.add_rec(recommended)

    def recommend(self):
        if bool_values[0]:
            return ["left 45", 1]
        elif bool_values[5]:
            return ["right 45", 1]
        elif bool_values[1]:
            return ["left 20", 0.9]
        elif bool_values[4]:
            return ["right 20", 0.9]
        else:
            return ["None", 0]

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
        recommended = self.recommend(value[0], value[1])
        self.bbcon.add_rec(recommended)

    def recommend(self, right, left):
        if right and not left:
            recommendation = ["left 45", 0.5]
        elif left and not right:
            recommendation = ["right 45", 0.5]
        else:
            recommendation = ["None", 0]
        return recommendation

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
