import numpy as np
import cv2

pix = np.uint8([[[255,0,0]]])

hsv = cv2.cvtColor(pix,cv2.COLOR_BGR2HSV)

print hsv
print pix