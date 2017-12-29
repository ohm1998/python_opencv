import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret ,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#hue saturation value
	lower_red = np.array([45,70,50])
	upper_red = np.array([90,200,200])
	mask = cv2.inRange(hsv,lower_red,upper_red)
	res = cv2.bitwise_and(frame,frame,mask = mask)
	# cv2.imshow('frame',frame)
	# cv2.imshow('mask',mask)
	cv2.imshow('Result',res)
	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break
cap.release()
cv2.destroyAllWindows()