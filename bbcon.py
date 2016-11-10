from zumo_button import ZumoButton as btn
from arbitrator import Arbitrator as ARB


button = btn()
m = motor()
def main():
    button.wait_for_press()
    m.forward(speed=0.5, dur=0.5)
    m.backward(speed=0.5, dur=0.5)    

main()

class BBCON:
    def __init__(self):
        self.ARB = ARB()
    
        self.behaviors = []         # all behaviors
        self.active = []            # active behaviors
        self.inactive = []          # inactive behaviors
        
        self.sensobs = []           # sensor objects
        self.motobs = []            # motor object(s), useless?!?!

        self.timestamp = 0
        self.motor_runtime = 0.5
        
    def add_behavior(self,b):
        self.behaviors.append(b)
    
    def add_sensob(self,s):
        self.sensobs.append(s)
    
    def activate(self,b):
        if b in self.inactive_behaviors and b in self.behaviors:
            self.active.append(b)
            self.inactive.remove(b)
    
    def deactivate(self,b):
        if b in self.active_behaviors and b in self.behaviors:
            self.inactive.append(b)
            self.active.remove(b)
            
    def run(self):
        current_data = []
        for sensor in self.sensobs:
            current_data.append(sensor, sensor.update()) # returnerer kun verdi
            # oppdaterer current_data med prioritet og verdi til enhver sensor
            # denne skal være en tuppel med (sensortype, verdi)
        self.ARB.choose_action(current_data)
        self.reset()
    
    def reset(self):
        self.timestamp += 1
        for sensor in self.sensobs:
            sensor.reset()