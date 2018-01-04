import numpy as np
import cv2

#Image Resizing

# img = cv2.imread('horse.png')

# res = cv2.resize(img,None,fx=0.5,fy=2, interpolation = cv2.INTER_CUBIC)

# cv2.imshow('Original',img)

# cv2.imshow('imageResize',res)

# cv2.waitKey(0)

img = cv2.imread('horse.png')

rows,cols,channel = img.shape

x= 80
img[(x-10):x,350] = [0,0,0]
pts1 = np.float32([[80,350],[300,350],[280,450],[80,450]])
pts2 = np.float32([[0,0],[200,0],[200,100],[0,100]])

m = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,m,(200,100))

cv2.imshow('Image',dst)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()