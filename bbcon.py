# from zumo_button import ZumoButton as btn
from arbitrator import Arbitrator as ARB
from motob import Motob
from behaviors import Follow_line, Avoid_collision, Avoid_walls
import time



# m = motor()

class BBCON:
    def __init__(self):
        self.ARB = ARB(self)
        self.recommendations = []
        self.motob = Motob()

        self.behaviors = set()         # all behaviors
        self.active = set()            # active behaviors
        self.inactive = set()          # inactive behaviors
        
        self.sensobs = set()
        self.motobs = [self.motob]            # motor object(s)
        
    def add_rec(self, r):
        self.recommendations.append(r)

    def add_behavior(self,b):
        self.behaviors.add(b)
        self.inactive.add(b)     # all behaviors are inactive be default
        

    def activate(self,b):
        if b in self.inactive and b in self.behaviors:
            print ('activating',b)
            self.active.add(b)
            self.inactive.remove(b)
            self.sensobs.add(b.get_sensob())

    def deactivate(self,b):
        if b in self.active and b in self.behaviors:
            print ('deactivating',b)
            self.inactive.add(b)
            self.active.remove(b)
            self.sensobs.remove(b.get_sensob())

    def run(self):

        del self.recommendations[:]

        # Update all sensobs
        print ('updating sensobs')
        for sensob in self.sensobs:
            print ('updating',sensob.__class__.__name__)
            sensob.update()

        # Update all behaviors
        print ('updating behaviors')
        for behavior in self.active:
            behavior.update()
            
        recommendation = self.ARB.choose_action()
        print ('recommendation = ',recommendation)

        # Update motobs
        for motob in self.motobs:
            motob.update(recommendation[0])
            # pass

        # Reset sensobs
        for sensob in self.sensobs:
            sensob.reset()
            

# class Main:

    # def __init__(self):
        # self.bbcon = BBCON()
        # self.follow_line = Follow_line(self.bbcon)
        # self.avoid_collision = Avoid_collision(self.bbcon)
        # self.avoid_walls = Avoid_walls(self.bbcon)
        # self.bbcon.add_behavior(self.follow_line)
        # self.bbcon.add_behavior(self.avoid_collision)
        # self.bbcon.add_behavior(self.avoid_walls)
        # answer = input("Would you like to activate follow_line? ")
        # if answer == 'y':
            # self.bbcon.activate(self.follow_line)
        # answer = input("Would you like to activate avoid_collision? ")
        # if answer == 'y':
            # self.bbcon.activate(self.avoid_collision)
        # answer = input("Would you like to activate avoid_walls? ")
        # if answer == 'y':
            # self.bbcon.activate(self.avoid_walls)

        # self.main()

    # def main(self):
        # while True:
            # self.bbcon.run()

            
def main():
    bbcon = BBCON()
    follow = Follow_line(bbcon)
    bbcon.add_behavior(follow)
    bbcon.activate(follow)
    
    avoid = Avoid_collision(bbcon)
    bbcon.add_behavior(avoid)
    bbcon.activate(avoid)
    
    camera = Avoid_walls(bbcon)
    bbcon.add_behavior(camera)
    bbcon.activate(camera)
    
    while True:
        bbcon.run()

main()