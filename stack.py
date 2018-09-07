class stack:
	def __init__(self):
		self.store=[]
	def push(self,val):
		self.store+=[val]
		return 0
	def pop(self):
		self.store=self.store[:len(self.store)-1]
		return 0
