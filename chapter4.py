#Shapes and Text
import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
# print(img)

# cv2.line(img,(0,0),(img.shape))
cv2.rect(img,(0,0),(250,350),(0,0,255),2)
cv2.imshow('Image',img)
cv2.waitKey(0)
