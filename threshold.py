import numpy as np
import cv2


img = cv2.imread("bookpage.jpg")

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("image_threshold",th)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()