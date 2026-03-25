#OpenCV
import numpy as np
import cv2
img=cv2.imread('test_image3.png')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img3=cv2.Canny(img2,275,325)
img5=cv2.erode(img3,(1,1),iterations=1)
#img7=cv2.medianBlur(img3,3)
img6=cv2.GaussianBlur(img3,(3,3),3)
#img4=cv2.dilate(img3,(7,7),iterations=1)
#img5=cv2.erode(img5,(7,7),iterations=2)
#cv2.imshow('Original',img)
#cv2.imshow('Gray',img2)
cv2.imshow('Canny',img3)
#cv2.imshow('Median Blurred of edges',img7)
cv2.imshow('Gaussian Blurred of edges',img6)
#cv2.imshow('Dilated',img4)
#cv2.imshow('Eroded',img5)
'''
a=img.shape
s=img[0:300,0:300]
img6=cv2.resize(img,(a[0]*2,a[1]*2))
cv2.imshow('Resized',img6)
cv2.imshow('Section',s)'''

cv2.waitKey(10000)