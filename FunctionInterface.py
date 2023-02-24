class lfunctionInterface():

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def valueAt(self, x):
		a = self.a
		b = self.b
		if(x < a): return 1.0
		elif(x >= b): return 0.0
		else: return (float)(b-x)/(b-a)

class gammaInterface():
	
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def valueAt(self, x):
		a = self.a
		b = self.b
		if(x<a): return 0.0
		elif(x >=b): return 1.0
		else: return (float)(x-a)/(b-a)

class lamInterface():

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def valueAt(self, x):
		a = self.a
		b = self.b
		c = self.c
		if(x < a): return 0.0
		elif(x >= a and x < b): return (float)(x-a)/(b-a)
		elif(x >= b and x <= c): return (float)(c-x)/(c-b)
		else: return 0.0

class uniformInterface():

	def __init__(self, a):
		self.a = a

	def valueAt(self, x):
		return self.a

class zadehNot():

	def __init__(self, function):
		self.function = function

	def valueAt(self, x):
		return 1 - self.function.valueAt(x)

class zadehOr():
	
	def __init__(self, function1, function2):
		self.f1 = function1
		self.f2 = function2

	def valueAt(self, x):
		a = self.f1.valueAt(x)
		b = self.f2.valueAt(x)
		if(a > b): return a
		else: return b

class zadehAnd():
	
	def __init__(self, function1, function2):
		self.f1 = function1
		self.f2 = function2

	def valueAt(self, x):
		a = self.f1.valueAt(x)
		b = self.f2.valueAt(x)
		if(a < b): return a
		else: return b


