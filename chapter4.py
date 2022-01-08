#Shapes and Text
import cv2
import numpy as np
#Creating a simple black image using numpy array
img=np.zeros((512,512,3),np.uint8)# 3 for giving color functionality
# print(img.shape)
# print(img)
# img[:]=255,0,0 #To color image to blue(B.G,R)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)#cv2.FILLED to fill the rectangle
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"This is a Text",(300,300),cv2.FONT_HERSHEY_PLAIN,1,(0,150,0),1)

cv2.imshow('Image',img)
cv2.waitKey(0)