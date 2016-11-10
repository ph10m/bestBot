from sensobs import IR_sensob, Reflenctance_sensob, Camera_sensob

class Follow_line:

	def __init__(self, bbcon):
		self.bbcon = bbcon
		self.sensor = Reflenctance_sensob()
		self.active_flag = False

	def update():
		value = self.sensor.get_value()
		bbcon.recommendations.append(value)

class Avoid_collision:

	def __init__(self, bbcon):
		self.bbcon = bbcon
		self.sensor = IR_sensob()
		self.active_flag = False

	def update():
		value = self.sensor.get_value()
		bbcon.recommendations.append(value)

class Avoid_walls:

	def __init__(self, bbcon):
		self.bbcon = bbcon
		self.sensor = Camera_sensob()
		self.active_flag = False

	def update():
		value = self.sensor.get_value()
		bbcon.recommendations.append(value)
