import cv2
import numpy as np

cap = cv2.VideoCapture(1)
#cap.open("http://192.168.43.1:8080/video?.mjpeg")
cv2.namedWindow('Colorbars')

def nothing(w):
	pass




x = 'Colorbars'


cv2.createTrackbar('HLOW',x,0,179,nothing)
cv2.createTrackbar('SLOW',x,0,255,nothing)
cv2.createTrackbar('VLOW',x,0,255,nothing)
cv2.createTrackbar('HHIGH',x,0,179,nothing)
cv2.createTrackbar('SHIGH',x,0,255,nothing)
cv2.createTrackbar('VHIGH',x,0,255,nothing)

















while(1):
	rect,frame = cap.read()
	roi =frame[100:420,100:480]
	#cv2.imshow('roi',roi)
	#roi =cv2.GaussianBlur(roi,(3,3),0)
	#imgray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
	#ret,thresh = cv2.threshold(imgray,127,255,0)
	hsv= cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
	cv2.imshow('frame',roi)	
	#median = cv2.medianBlur(hsv,9)
	


	hl = cv2.getTrackbarPos('HLOW',x)
	hh = cv2.getTrackbarPos('HHIGH',x)
	sl = cv2.getTrackbarPos('SLOW',x)
	sh = cv2.getTrackbarPos('SHIGH',x)
	vl = cv2.getTrackbarPos('VLOW',x)
	vh = cv2.getTrackbarPos('VHIGH',x)



	lower_ball = np.array([hl,sl,vl])
	upper_ball = np.array([hh,sh,vh])
	
	
	mask = cv2.inRange(hsv,lower_ball,upper_ball)
	median = cv2.medianBlur(mask,9)
	cv2.imshow('mask',median)

	cv2.circle(hsv,(62,195), 30, (0,0,255), 2)
	xyzx =  hsv[62,195]
	#print xyzx[0]
	#res = cv2.bitwise_and(roi,roi,mask=mask)
	#imgray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
        #ret,thresh = cv2.threshold(imgray,127,255,0)
	
	#cv2.imshow('res',res)	
	
	
	#_,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	#cv2.drawContours(res, contours, -1, (0,255,0), 1)

	#cnt = contours[0]
	#M = cv2.moments(cnt)

	#cx = int(M['m10']/M['m00'])
	#cy = int(M['m01']/M['m00'])
	#print cx,cy
	#M = cv2.moments(cnt)
	#print M
	#if cy<350:
	#	print "forward"
	#if cx<200:
	#	print "left"
	#area = cv2.contourArea(cnt)
	#print area	
	#cv2.drawContours(frame,contours ,-1 , (0,255,0), 10)
	#x = len(contours)
	#print x
	
	#cv2.imshow('roi',res)
        #cv2.imshow('mask',mask)
        #cv2.imshow('res',res)
	

	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break
cv2.destroyAllWindows()
