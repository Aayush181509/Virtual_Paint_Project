# Basic Functions 
import cv2
import numpy as np

img=cv2.imread('resources/image1.jpg')
kernel=np.ones((5,5),np.uint8) # Creating kernel

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#Converting normal image to greyscale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Image Canny",imgEroded)
cv2.waitKey(0)


