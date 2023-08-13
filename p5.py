import cv2
import numpy as np

img=cv2.imread('img.jpg',0)

eq_img=cv2.equalizeHist(img)
thresh=cv2.adaptiveThreshold(eq_img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,2)
kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel)

cv2.imshow('original image',img)
cv2.imshow('equalized image',eq_img)
cv2.imshow('segemeted image', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()