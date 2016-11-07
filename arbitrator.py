from motob import Motob as MOTOR

class Arbitrator:
    def __init__(self):
        self.current_motor_rec = None
        self.motor = MOTOR()
        
    def choose_action(self, sensors):
        # hent ut den høyst prioriterte sensoren ut fra lista
        # og lag så en "motor recommendation"
        sensor_type,value = max(sensors, key=itemgetter(1))
        self.motor.run(sensor_type,value)
        self.wait()
        
    def wait(self):
        # implementer threading?
        pass
