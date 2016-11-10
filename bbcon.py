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
        self.ARB = ARB(self)

        self.behaviors = []         # all behaviors
        self.active = []            # active behaviors
        self.inactive = []          # inactive behaviors

        self.sensobs = []           # sensor objects
        self.motobs = []            # motor object(s), useless?!?!
        self.recommendations = []

        self.timestamp = 0
        self.motor_runtime = 0.5

    def add_behavior(self,b):
        self.behaviors.append(b)
        self.inactive.append(b)     # all behaviors are inactive be default

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

        # Update all sensobs
        for sensob in self.sensobs:
            sensob.update()

        # Update all behaviors
        for behavior in self.behaviors:
            

        recommendations = arbitrator.choose_action(self.sensobs)

        # Update motobs

        # Wait

        # Reset sensobs



    def reset(self):
        self.timestamp += 1
        for sensor in self.sensobs:
            sensor.reset()
