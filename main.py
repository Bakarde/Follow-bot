#! /usr/bin/env python
from Domain import SimpleDomain
from FuzzySet import *
import cv2
from FuzzyTypes import *
import os
from FuzzySystem import *


dm = SimpleDomain(range(10))
dm2 = SimpleDomain(range(10))
dm3 = SimpleDomain(range(11))

print(dm == dm2)
print(dm == dm3)

print(dm)

dm.setValues(range(15))
print(dm)

g = lam(5,10,20)
print(g.valueAt(12))
z = zadehNot(g)
print(z.valueAt(12))


l = lam(5,10,15)
l2 = lam(-5,0,5)

zand = zadehAnd(l,l2)
print(z.valueAt(10))

PATH = os.path.dirname(__file__)

vid = cv2.VideoCapture(0)
while(True):
	ret, frame = vid.read()
	cv2.imshow('frame', frame)

	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	haar_cascade = cv2.CascadeClassifier(os.path.join(PATH, "haarcascade_frontalface_default.xml"))
	faces_rect = haar_cascade.detectMultiScale(gray_img)
	if(len(faces_rect)>0):
		x,y,w,h = faces_rect[0]
		frame = cv2.rectangle(frame, (x, y), (x+w, y+h), color=(255,0,0), thickness=2)
		povrsina = (float)(w*h)/1000
		mid_x = (x+x+w)/2

		#conclude
		conclusion = rule_base_angular(mid_x, povrsina)
		conclusion2 = rule_base_linear(povrsina)
		print("kutna brzina..." + str(conclude_angular(conclusion)))
		
		print("linearna brzina... " + str(conclude_linear(conclusion2)))
	cv2.imshow("ja", frame) 
  
	# Displaying the image 
	
    	
    	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
