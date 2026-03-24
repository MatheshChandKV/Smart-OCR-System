#OpenCV
import numpy as np
import cv2
img=cv2.imread('test_image.png')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img3=cv2.GaussianBlur(img2,(7,7),0)
img4=cv2.Canny(img,275,300)
img5=cv2.dilate(img4,(7,7),iterations=1)
img6=cv2.erode(img5,(7,7),iterations=2)
#cv2.imshow('image',img)
#cv2.imshow('image3',img3)
#cv2.imshow('image2',img2)
cv2.imshow('image4',img4)
cv2.imshow('image5',img5)
cv2.imshow('image6',img6)
cv2.waitKey(20000)