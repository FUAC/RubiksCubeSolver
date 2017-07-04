import cv2
import numpy as np
import time
sq_red = []
sq_orange = []
sq_green = []
sq_yellow = []
sq_blue = []
sq_white = []
list1 = ['0','0','0','0','0','0','0','0','0']
cap = cv2.VideoCapture(1)

file = open("output",'a')

while True:
	ret,frame =  cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	roi = hsv[100:420,100:480]
	
	mask_red = cv2.inRange(roi,(164,128,0),(179,255,197))
	mask_orange = cv2.inRange(roi,(0,125,158),(10,196,255))
	mask_green = cv2.inRange(roi,(55,148,112),(108,255,204))
	mask_white = cv2.inRange(roi,(52,0,61),(165,129,255))
	mask_yellow = cv2.inRange(roi,(15,55,142),(47,195,240))
	mask_blue = cv2.inRange(roi,(8,130,52),(150,215,206))
	#cv2.imshow('mask',mask_red)
	mr = cv2.medianBlur(mask_red,9)
	median_orange = cv2.medianBlur(mask_orange,9)
	median_green = cv2.medianBlur(mask_green,9)
	median_blue = cv2.medianBlur(mask_blue,9)
	median_white = cv2.medianBlur(mask_white,9)	
	median_yellow = cv2.medianBlur(mask_yellow,9)
	cv2.imshow('red',mr)
	cv2.imshow('orange',median_orange)
	cv2.imshow('green',median_green)
	cv2.imshow('blue',median_blue)
	cv2.imshow('white',median_white)
	cv2.imshow('yellow',median_yellow)



	sq_1 = mr[50:100,50:100]
	
	cv2.rectangle(roi,(50,50),(100,100),(255,0,0),3)
	sq_2 = mr[50:100,165:215]
	cv2.rectangle(roi,(165,50),(215,100),(255,0,0),3)
	sq_3 = mr[50:100,280:330]
	cv2.rectangle(roi,(280,50),(330,100),(255,0,0),3)
	sq_4 = mr[165:215,50:100]
	cv2.rectangle(roi,(50,165),(100,215),(255,0,0),3)
	sq_5 = mr[165:215,165:215]
        cv2.rectangle(roi,(165,165),(215,215),(255,0,0),3)      	
	sq_6 = mr[165:215,280:330]
        cv2.rectangle(roi,(280,165),(330,215),(255,0,0),3)      
	sq_7 = mr[280:330,50:100]
        cv2.rectangle(roi,(50,280),(100,330),(255,0,0),3)      
	sq_8 = mr[280:330,165:215]
        cv2.rectangle(roi,(165,280),(215,330),(255,0,0),3)      
	sq_9 = mr[280:330,280:330]
        cv2.rectangle(roi,(280,280),(330,330),(255,0,0),3)      


	


	pr1 = sq_1[25,25]
	pr2 = sq_2[25,25]
	pr3 = sq_3[25,25]
	pr4 = sq_4[25,25]
	pr5 = sq_5[25,25]
	pr6 = sq_6[25,25]
	pr7 = sq_7[25,25]
	pr8 = sq_8[25,25]
	pr9 = sq_9[25,25]



	sq_red = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,pr9]
	
	for i in range(0,9):
		if(sq_red[i]==255):
			print "red@",i+1
                 	list1[i] = 'U'







	





	sq_1 = median_orange[50:100,50:100]
	
	cv2.rectangle(roi,(50,50),(100,100),(255,0,0),3)
	sq_2 = median_orange[50:100,165:215]
	cv2.rectangle(roi,(165,50),(215,100),(255,0,0),3)
	sq_3 = median_orange[50:100,280:330]
	cv2.rectangle(roi,(280,50),(330,100),(255,0,0),3)
	sq_4 = median_orange[165:215,50:100]
	cv2.rectangle(roi,(50,165),(100,215),(255,0,0),3)
	sq_5 = median_orange[165:215,165:215]
        cv2.rectangle(roi,(165,165),(215,215),(255,0,0),3)      	
	sq_6 = median_orange[165:215,280:330]
        cv2.rectangle(roi,(280,165),(330,215),(255,0,0),3)      
	sq_7 = median_orange[280:330,50:100]
        cv2.rectangle(roi,(50,280),(100,330),(255,0,0),3)      
	sq_8 = median_orange[280:330,165:215]
        cv2.rectangle(roi,(165,280),(215,330),(255,0,0),3)      
	sq_9 = median_orange[280:330,280:330]
        cv2.rectangle(roi,(280,280),(330,330),(255,0,0),3)      


	po1 = sq_1[25,25]
	po2 = sq_2[25,25]
	po3 = sq_3[25,25]
	po4 = sq_4[25,25]
	po5 = sq_5[25,25]
	po6 = sq_6[25,25]
	po7 = sq_7[25,25]
	po8 = sq_8[25,25]
	po9 = sq_9[25,25]

	sq_orange = [po1,po2,po3,po4,po5,po6,po7,po8,po9]

	for i in range(0,9):
		if(sq_orange[i]==255):
			print "orange@",i+1
			list1[i] = 'D'
			#print list1




		 


	sq_1 = median_green[50:100,50:100]
	
	cv2.rectangle(roi,(50,50),(100,100),(255,0,0),3)
	sq_2 = median_green[50:100,165:215]
	cv2.rectangle(roi,(165,50),(215,100),(255,0,0),3)
	sq_3 = median_green[50:100,280:330]
	cv2.rectangle(roi,(280,50),(330,100),(255,0,0),3)
	sq_4 = median_green[165:215,50:100]
	cv2.rectangle(roi,(50,165),(100,215),(255,0,0),3)
	sq_5 = median_green[165:215,165:215]
        cv2.rectangle(roi,(165,165),(215,215),(255,0,0),3)      	
	sq_6 = median_green[165:215,280:330]
        cv2.rectangle(roi,(280,165),(330,215),(255,0,0),3)      
	sq_7 = median_green[280:330,50:100]
        cv2.rectangle(roi,(50,280),(100,330),(255,0,0),3)      
	sq_8 = median_green[280:330,165:215]
        cv2.rectangle(roi,(165,280),(215,330),(255,0,0),3)      
	sq_9 = median_green[280:330,280:330]
        cv2.rectangle(roi,(280,280),(330,330),(255,0,0),3)      




	pg1 = sq_1[25,25]
	pg2 = sq_2[25,25]
	pg3 = sq_3[25,25]
	pg4 = sq_4[25,25]
	pg5 = sq_5[25,25]
	pg6 = sq_6[25,25]
	pg7 = sq_7[25,25]
	pg8 = sq_8[25,25]
	pg9 = sq_9[25,25]
	print pg9


	sq_green = [pg1,pg2,pg3,pg4,pg5,pg6,pg7,pg8,pg9]

	for i in range(0,9):
		if(sq_green[i]==255):
			print "green@",i+1
			list1[i] = 'R'


	sq_1 = median_blue[50:100,50:100]
	
	cv2.rectangle(roi,(50,50),(100,100),(255,0,0),3)
	sq_2 = median_blue[50:100,165:215]
	cv2.rectangle(roi,(165,50),(215,100),(255,0,0),3)
	sq_3 = median_blue[50:100,280:330]
	cv2.rectangle(roi,(280,50),(330,100),(255,0,0),3)
	sq_4 = median_blue[165:215,50:100]
	cv2.rectangle(roi,(50,165),(100,215),(255,0,0),3)
	sq_5 = median_blue[165:215,165:215]
        cv2.rectangle(roi,(165,165),(215,215),(255,0,0),3)      	
	sq_6 = median_blue[165:215,280:330]
        cv2.rectangle(roi,(280,165),(330,215),(255,0,0),3)      
	sq_7 = median_blue[280:330,50:100]
        cv2.rectangle(roi,(50,280),(100,330),(255,0,0),3)      
	sq_8 = median_blue[280:330,165:215]
        cv2.rectangle(roi,(165,280),(215,330),(255,0,0),3)      
	sq_9 = median_blue[280:330,280:330]
        cv2.rectangle(roi,(280,280),(330,330),(255,0,0),3)      



	pb1 = sq_1[25,25]
	pb2 = sq_2[25,25]
	pb3 = sq_3[25,25]
	pb4 = sq_4[25,25]
	pb5 = sq_5[25,25]
	pb6 = sq_6[25,25]
	pb7 = sq_7[25,25]
	pb8 = sq_8[25,25]
	pb9 = sq_9[25,25]


	sq_blue = [pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8,pb9]

	for i in range(0,9):
		if(sq_blue[i]==255):
			print "blue@",i+1
			list1[i] = 'L'


	sq_1 = median_white[50:100,50:100]
	
	cv2.rectangle(roi,(50,50),(100,100),(255,0,0),3)
	sq_2 = median_white[50:100,165:215]
	cv2.rectangle(roi,(165,50),(215,100),(255,0,0),3)
	sq_3 = median_white[50:100,280:330]
	cv2.rectangle(roi,(280,50),(330,100),(255,0,0),3)
	sq_4 = median_white[165:215,50:100]
	cv2.rectangle(roi,(50,165),(100,215),(255,0,0),3)
	sq_5 = median_white[165:215,165:215]
        cv2.rectangle(roi,(165,165),(215,215),(255,0,0),3)      	
	sq_6 = median_white[165:215,280:330]
        cv2.rectangle(roi,(280,165),(330,215),(255,0,0),3)      
	sq_7 = median_white[280:330,50:100]
        cv2.rectangle(roi,(50,280),(100,330),(255,0,0),3)      
	sq_8 = median_white[280:330,165:215]
        cv2.rectangle(roi,(165,280),(215,330),(255,0,0),3)      
	sq_9 = median_white[280:330,280:330]
        cv2.rectangle(roi,(280,280),(330,330),(255,0,0),3)      



	
	pw1 = sq_1[25,25]
	pw2 = sq_2[25,25]
	pw3 = sq_3[25,25]
	pw4 = sq_4[25,25]
	pw5 = sq_5[25,25]
	pw6 = sq_6[25,25]
	pw7 = sq_7[25,25]
	pw8 = sq_8[25,25]
	pw9 = sq_9[25,25]


	sq_white = [pw1,pw2,pw3,pw4,pw5,pw6,pw7,pw8,pw9]

	for i in range(0,9):
		if(sq_white[i]==255):
			print "white@",i+1
			list1[i] = 'F'



	sq_1 = median_yellow[50:100,50:100]
	
	cv2.rectangle(roi,(50,50),(100,100),(255,0,0),3)
	sq_2 = median_yellow[50:100,165:215]
	cv2.rectangle(roi,(165,50),(215,100),(255,0,0),3)
	sq_3 = median_yellow[50:100,280:330]
	cv2.rectangle(roi,(280,50),(330,100),(255,0,0),3)
	sq_4 = median_yellow[165:215,50:100]
	cv2.rectangle(roi,(50,165),(100,215),(255,0,0),3)
	sq_5 = median_yellow[165:215,165:215]
        cv2.rectangle(roi,(165,165),(215,215),(255,0,0),3)      	
	sq_6 = median_yellow[165:215,280:330]
        cv2.rectangle(roi,(280,165),(330,215),(255,0,0),3)      
	sq_7 = median_yellow[280:330,50:100]
        cv2.rectangle(roi,(50,280),(100,330),(255,0,0),3)      
	sq_8 = median_yellow[280:330,165:215]
        cv2.rectangle(roi,(165,280),(215,330),(255,0,0),3)      
	sq_9 = median_yellow[280:330,280:330]
        cv2.rectangle(roi,(280,280),(330,330),(255,0,0),3)      



	py1 = sq_1[25,25]
	py2 = sq_2[25,25]
	py3 = sq_3[25,25]
	py4 = sq_4[25,25]
	py5 = sq_5[25,25]
	py6 = sq_6[25,25]
	py7 = sq_7[25,25]
	py8 = sq_8[25,25]
	py9 = sq_9[25,25]


	sq_yellow = [py1,py2,py3,py4,py5,py6,py7,py8,py9]

	for i in range(0,9):
		if(sq_yellow[i]==255):
			print "yellow@",i+1
		
			list1[i] = 'B'
	







	flag=0
	for j in range(0,9):
		if(list1[j]== '0'):
			flag=1	
		
	if(flag==0):
		print list1
		str = ''.join(list1)
		print str
		file.write(str)
		file.close()		
		exit()
		


  
	

	cv2.imshow('roi',roi)
	#print list1
		

	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break


cv2.destroyAllWindows()
