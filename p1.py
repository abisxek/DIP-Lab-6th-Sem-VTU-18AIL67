import cv2
img=cv2.imread("img.JPG")
height,width=img.shape[:2]
center_x,center_y=int(width/2),int(height/2)

top_left=img[0:center_y,0:center_x]
top_right=img[0:center_y,center_x:width]
bottom_left=img[center_y:height,0:center_x]
bottom_right=img[center_y:height,center_x:width]

#not necessary
cv2.namedWindow("topleft",cv2.WINDOW_NORMAL)
cv2.namedWindow("topright",cv2.WINDOW_NORMAL)
cv2.namedWindow("bottomleft",cv2.WINDOW_NORMAL)
cv2.namedWindow("bottomright",cv2.WINDOW_NORMAL)
#not necessary
cv2.resizeWindow("topleft",400,400)
cv2.resizeWindow("topright",400,400)
cv2.resizeWindow("bottomleft",400,400)
cv2.resizeWindow("bottomright",400,400)

cv2.imshow("topleft",top_left)
cv2.imshow("topright",top_right)
cv2.imshow("bottomleft",bottom_left)
cv2.imshow("bottomright",bottom_right)
cv2.waitKey(0)
cv2.destroyAllWindows()