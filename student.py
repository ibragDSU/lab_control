class Student:

	def __init__(self, first, last, labs, v):
		self.first = first
		self.last = last
		self.labs = labs
		self.v = v

	def get_fullname(self):
		return f'{self.first.title()} {self.last.title()}'

	def __repr__(self):
		return f'Student ({self.get_fullname}, v = {self.v}, labs amount = {len(self.labs)})'
