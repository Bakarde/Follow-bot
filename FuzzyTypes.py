import math
from enum import Enum
from FuzzySet import *
from Domain import SimpleDomain

class Side(Enum):
	domain = (0,640)
	LL = lfunction(100,240)
	L = lam(100,240,320)
	M = lam(240,320,400)
	R = lam(320,400,480)
	RR = gamma(400,540)

class BB(Enum):
	domain = (0,300) #300 jer je max povrsina 307000 pa podijeljeno s 1000 daje otprilike max 300
	XS = lfunction(5,10)
	S = lam(5,10,15)
	M = lam(10,20,30)
	L = lam(20,35,50)
	XL = gamma(35,80)

class LV(Enum):
	domain = (-2, 2)
	XXS = lfunction(-1.5,-1)
	XS = lam(-1.5,-1,-0.5)
	S = lam(-1,-0.5,0)
	M = lam(-0.5,0,0.5)
	L = lam(0,0.5,1)
	XL = lam(0.5,1,1.5)
	XXL = gamma(1,1.5)

class AV(Enum):
	domain = (-1.5,1.5)
	XXS = lfunction(-1.0, -0.75)
	XS = lam(-1.0,-0.75,-0.25)
	S = lam(-0.75, -0.25,0)
	M = lam(-0.25,0.0,0.25)
	L = lam(0,0.25,0.75)
	XL = lam(0.25,0.75,1.0)
	XXL = gamma(0.75,1.0)
