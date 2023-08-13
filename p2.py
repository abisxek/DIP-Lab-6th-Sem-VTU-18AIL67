import cv2
import numpy as np

img =cv2.imread('img.jpg')
print("size of original image: height width",img.shape[:2])

rows,cols =img.shape[:2]
M=cv2.getRotationMatrix2D((cols/2, rows/2), 45,1)
rotated_img=cv2.warpAffine(img,M,(cols,rows))
scaled_img=cv2.resize(img,None,fx=0.01,fy=0.01,interpolation=cv2.INTER_LINEAR)
print("size of scaled image: height, width",scaled_img.shape[:2])

M=np.float32([[1,0,100],[0,1,50]])
translated_img=cv2.warpAffine(img,M,(cols,rows))

#not necessary
cv2.namedWindow('original image', cv2.WINDOW_NORMAL)
cv2.namedWindow('rotated image', cv2.WINDOW_NORMAL)
cv2.namedWindow('scaled image', cv2.WINDOW_NORMAL)
cv2.namedWindow('translated image', cv2.WINDOW_NORMAL)
#not necessary
cv2.resizeWindow('original image', 300, 300)
cv2.resizeWindow('rotated image', 300, 300)
cv2.resizeWindow('scaled image', 300, 300)
cv2.resizeWindow('translated image', 300, 300)

cv2.imshow("original image",img)
cv2.imshow("rotated image",rotated_img)
cv2.imshow("scaled image",scaled_img)
cv2.imshow("translated image",translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()