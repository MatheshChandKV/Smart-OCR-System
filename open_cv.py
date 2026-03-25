#OpenCV
import cv2
img=cv2.imread('test_image6.png')
b_img=cv2.imread('black screen.png')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
gray = clahe.apply(img2)
img3=cv2.GaussianBlur(img2,(3,3),1)
thresh = cv2.adaptiveThreshold(
    img3, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)
kernel = (2,2)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
img4=cv2.dilate(img3,kernel,iterations=2)
#cv2.imshow('Original',img)
cv2.imshow('pre-processed image',img4)
cv2.waitKey(0)
#cv2.imshow('Dilated',img4)
#cv2.imshow('Eroded',img5)
#cv2.imshow('Median Blurred of edges',img7)

