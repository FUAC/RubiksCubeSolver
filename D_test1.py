import cv2
import numpy as np
import os,sys,json
import time 
from math import *


path_to_library = os.path.join(os.path.dirname(__file__),"httplib2/python2")
sys.path.append(path_to_library)

import httplib2
import kociemba


def stepper(str):
	
	http = httplib2.Http()
	url_json = "http://192.168.43.44/stepper"
	headers = {"Content-Type":"application/json; charset=UTF-8"}
	data = {"cube":str}
	response,content = http.request(url_json,"POST",headers=headers,body=json.dumps(data))
	return


#def recursive(x):
	#x = 0
	#y = input("NEXT FACE PLAESE: ")
	#if(y==0):
		 
		#return
		




cap = cv2.VideoCapture()
cap.open("http://192.168.1.101:8080/video?.mjpeg")
time.sleep(5)
list = []
h = [[[[]]]]
hsv = [[[[]]]]
s= ""
m = []
x = 0
while(1):
	x = 0
	print x
	
	
	ret,frame = cap.read()
	cv2.circle(frame,(975,525), 30, (0,0,255), 2)
	cv2.circle(frame,(1075,525),30,(0,0,255),2)
	cv2.circle(frame,(1175,525), 30, (0,0,255), 2)
	cv2.circle(frame,(975,725), 30, (0,0,255), 2)
	cv2.circle(frame,(1075,625), 30, (0,0,255), 2)
	cv2.circle(frame,(1075,725), 30, (0,0,255), 2)
	cv2.circle(frame,(1175,525), 30, (0,0,255), 2)
	cv2.circle(frame,(1175,625), 30, (0,0,255), 2)
	cv2.circle(frame,(1175,725), 30, (0,0,255), 2)
	cv2.circle(frame,(975,625), 30, (0,0,255), 2)
	

	px1 = frame[400,400]
	px2 = frame[400,500]
	px3 = frame[400,600]
	px4 = frame[500,400]
	px5 = frame[500,500]
	px6 = frame[500,600]
	px7 = frame[600,400]
	px8 = frame[600,500]
	px9 = frame[600,600]  
	
	
 
	
	list = [px1,px2,px3,px4,px5,px6,px7,px8,px9]
	for i in range(len(list)):
		if(list[i][0]>170 and list[i][1]>170 and list[i][2]>170 and x<9):
			print "white"
			s+= 'F'
			x=len(s)
			print x
			if( x== 54):
				k = kociemba.solve(s)
				stepper(k)
				#stepper(s)
				break
		if(list[i][0]>100 and list[i][1]<100 and list[i][2]<100 and x<9):
			print "blue"
			s+= 'L'
			x=len(s)
			if( x== 54):
				k = kociemba.solve(s)
				stepper(k)
				#stepper(s)
				break
		if(list[i][0]<100 and list[i][1]<110 and list[i][2]>200 and x<9):
			print "orange"
			s+= 'D'
			x=len(s)
			if( x== 54):
				k = kociemba.solve(s)
				stepper(k)
				#stepper(s)
				break
		if(list[i][0]<90 and list[i][1]<90 and list[i][2]>130 and x<9):
			print "red"
			s+= 'U'
			x=len(s)
			if( x== 54):
				k = kociemba.solve(s)
				stepper(k)
				#stepper(s)
				break
		if(list[i][0]<40 and list[i][1]>150 and list[i][2]>200 and x<9):
			print "yellow"
			s+= 'B'
			x=len(s)
			if( x== 54):
				stepper(s)
				break
		if(list[i][0]<40 and list[i][1]<40 and list[i][2]>120 and x<9):
			print "green"
			s+= 'G'
			x=len(s)
			if( x== 54):
				k = kociemba.solve(s)
				stepper(k)
				#stepper(s)
				
				break	
		
		#print x
			
				
				
					
				
		#print list[i]
	#for i in range(len(list)-1):
		#h[i] = np.uint8([[list[i]]])
		#hsv[i] = cv2.cvtColor(h[i],cv2.COLOR_BGR2HSV)
		#print list[i]	
	#print hsv		
		
	
		
	cv2.imshow('frame',frame)
	if(x==9):
		#recursive(x)
		y = input("Right Face: ")
	if(x==18):	
		b = input("Front face: ")
	if(x==27):
		c = input("Down Face: ")
	if(x==36):
		d = input("Left Face: ")
	if(x==45):
		e = input("Back Face: ")
	if(x==54):
		print s
		break		
			
					
		
			
	
	
	
	
	
	k = cv2.waitKey(5) & 0xFF
        if k==27:
                break
cv2.destroyAllWindows()

