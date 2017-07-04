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
cap.open("http://192.168.1.100:8080/video?.mjpeg")
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
	
	px=[[0 for x in range(2)] for x in range(9)]	
	
	px[0][0]=875
	px[0][1]=500
	px[1][0]=1060
	px[1][1]=500
	px[2][0]=1250
	px[2][1]=500
	px[3][0]=875
	px[3][1]=700
	px[4][0]=1250
	px[4][1]=700
	px[5][0]=1250
	px[5][1]=700
	px[6][0]=875
	px[6][1]=900
	px[7][0]=1250
	px[7][1]=900
	px[8][0]=1250
	px[8][1]=900
	
	
	ret,frame = cap.read()
	cv2.circle(frame,(px[0][0],px[0][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[1][0],px[1][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[2][0],px[2][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[3][0],px[3][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[4][0],px[4][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[5][0],px[5][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[6][0],px[6][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[7][0],px[7][1]), 30, (0,0,255), 2)
	cv2.circle(frame,(px[8][0],px[8][1]), 30, (0,0,255), 2)
	

	px1 = frame[px[0][0],px[0][1]]
	px2 = frame[px[1][0],px[1][1]]
	px3 = frame[px[2][0],px[2][1]]
	px4 = frame[px[3][0],px[3][1]]
	px5 = frame[px[4][0],px[4][1]]
	px6 = frame[px[5][0],px[5][1]]
	px7 = frame[px[6][0],px[6][1]]
	px8 = frame[px[7][0],px[7][1]]
	px9 = frame[px[8][0],px[8][1]]  
	
	
 
	
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
