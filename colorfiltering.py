import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret ,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#hue saturation value
	lower = {'red': 50, 'green': 50 ,'blue' : 50} 
	upper = {'red': 100 , 'green': 100 ,'blue' : 150}
	lower_pix = np.uint8([[[lower['blue'],lower['green'],lower['red']]]]); 
	upper_pix = np.uint8([[[upper['blue'],upper['green'],upper['red']]]]); 
	lower_pix = cv2.cvtColor(lower_pix,cv2.COLOR_BGR2HSV)
	upper_pix = cv2.cvtColor(upper_pix,cv2.COLOR_BGR2HSV)
	#print upper_pix
	#print lower_pix
	mask = cv2.inRange(hsv,lower_pix,upper_pix)
	res = cv2.bitwise_and(frame,frame,mask = mask)
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask,kernel,iterations=1)
	dilation = cv2.dilate(mask,kernel,iterations=1)

	opening = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernel)
	closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)


	closing = cv2.GaussianBlur(closing,(5,5),0)
	closing = cv2.medianBlur(closing,5)
	res = cv2.bitwise_and(frame,frame,mask = closing)
	#cv2.imshow('Mask',mask)
	#cv2.imshow('opening',opening)
	#cv2.imshow('Closing',closing)
	cv2.imshow("Final",res)
	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break
cap.release()
cv2.destroyAllWindows()