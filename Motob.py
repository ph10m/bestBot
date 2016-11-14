from motors import Motors
from random import randint
import time

class Motob:

    def __init__(self):
        self.motor = Motors()
        self.value = -1
        self.speed = 0.35
        self.funcs = {
            "left": self.left,
            "right": self.right,
            "random": self.random,
            "rewind": self.rewind
        }

    def update(self, recommendation):
        print ('operating',recommendation,'in motobs')
        self.operate(recommendation)

    def operate(self, recommended):
        if recommended == "None":
            self.wander()
        else:
            func, self.value = recommended.split(" ")
            self.value = int(self.value)
            if func in self.funcs:
                self.funcs[func]()
            else:
                self.wander()

    def wander(self):
        self.motor.forward(speed = self.speed, dur = 0.15)

    def degree_to_duration(self, degrees):
        # 0.75 per runde på full speed
        # anta halv speed, så ca 1.5 sec per runde
        time_per_round = 2.5
        time_per_degree = time_per_round/360
        return degrees*time_per_degree

    def get_degrees(self):
        return self.degree_to_duration(self.value)

    def left(self):
        self.motor.left(speed=self.speed*2, dur=self.get_degrees())

    def right(self):
        self.motor.right(speed=self.speed*2, dur=self.get_degrees())

    def random(self):
        # turn left or right by random
        # turn 90 degrees regardless
        self.value = 90
        if randint(0,100)>50:
            self.right()
        else:
            self.left()

    def rewind(self):
        # run back for a while
        if self.value <= 0:
            self.value = 1      # set a default value
        self.motor.backward(speed=self.speed, dur = self.value)
            