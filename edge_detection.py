import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret ,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#hue saturation value
	# laplacian = cv2.Laplacian(frame,cv2.CV_64F)
	# sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize = 5)
	# sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize = 5)

	edges  = cv2.Canny(frame,100,100)
	edges = cv2.GaussianBlur(edges,(5,5),0)
	cv2.imshow("Edges",edges)


	# cv2.imshow('Laplacian',laplacian)
	# cv2.imshow('SobelX',sobelx)
	# cv2.imshow('SobelY',sobely)

	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break
cap.release()
cv2.destroyAllWindows()