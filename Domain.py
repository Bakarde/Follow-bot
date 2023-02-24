#! /usr/bin/env python

class SimpleDomain():
	
	def __init__(self, values):
		self.values = values

	

	def __eq__(self, obj):
		if(not isinstance(obj, SimpleDomain)):
			return False

		if(len(self.values) != len(obj.values)):
			return False
		
		for i,j in zip(self.values, obj.values):
			if(i != j):
				return False
		return True
	def __str__(self):
		return str(self.values)

	def setValues(self, values):
		self.values = values

	def getComponentValue(self, index):
		return self.values[index]
