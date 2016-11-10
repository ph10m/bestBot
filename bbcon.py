from zumo_button import ZumoButton as btn
from arbitrator import Arbitrator as ARB
import time


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
        self.motobs = []            # motor object(s)

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
            behavior.update()               # Sjekk om dette funker!

        recommendation = self.ARB.choose_action()

        # Update motobs
        for motob in self.motobs:
            motob.update(recommendation)

        # Wait
        time.sleep(0.3)

        # Reset sensobs
        for sensob in self.sensobs:
            sensob.reset()
