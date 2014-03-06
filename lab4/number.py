class integer(object):
	def __init__(self, number):
		self.number = number
	def display(self):
		print self.number

if __name__=="__main__":
	d = integer(4)
	d.display()
