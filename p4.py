import cv2
import numpy as np

img = cv2.imread("img.jpg",cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(img, (3, 3),0)

edges = cv2.Canny(blur, 50, 150)

sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3) 
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3) 
texture = np.sqrt(sobelx**2+sobely**2)
texture = np.uint8(texture)

#named window and resize window optional
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image", 300, 300)
cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Edges", 300, 300)
cv2.namedWindow("Texture", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Texture", 300, 300)

cv2.imshow("Texture", texture) 
cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()