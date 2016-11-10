from motors import Motors
class Motob:
    def __init__(self):
        self.motor = Motors()
        self.recommendation
        self.funcs = {
            left: self.left,
            right: self.right,
            random: self.random,
            rewind: self.rewind
        }
        self.value = -1
        self.speed = 0.5
        
	def update(self, recommendation):
		self.operate(recommendation)
		
	def operate(recommended):
        func, self.value = recommended.split(" ")
        if func in funcs:
            self.funcs[func]()
        else:
            self.wander()
            
    def wander(self):
        self.motors.forward(speed = self.speed, dur = 5)
    
    def degree_to_duration(self, degrees):
        # 0.75 per runde på full speed
        # anta halv speed, så ca 1.5 sec per runde
        time_per_round = 1.5
        time_per_degree = 1.5/360
        return degree*time_per_degree
        
    def get_degrees():
        return self.degree_to_duration(self.value)
    
    def left(self):
        self.motor.left(speed=self.speed, self.get_degrees())
        
    def right(self):
        self.motor.right(speed=self.speed, self.get_degrees())
        
    from random import randint
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
            self.value = 2      # set a default value
        self.motor.backward(speed=self.speed, self.value)
            