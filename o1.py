import numpy as np
import cv2
cap = cv2.VideoCapture('trial.mp4')

while(True):
	ret, frame = cap.read()
	
	ret = cap.set(3,360);
	ret = cap.set(4,360);
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()