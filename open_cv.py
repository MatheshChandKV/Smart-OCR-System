#OpenCV
import cv2
img=cv2.imread('test_image2.png')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img3=cv2.GaussianBlur(img2,(67,67),0)
cv2.imshow('image',img)
cv2.imshow('image3',img3)
cv2.imshow('image2',img2)
cv2.waitKey(5000)