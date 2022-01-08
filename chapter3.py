# Crop and Resize
import cv2
import numpy as np

img=cv2.imread('Resources/image1.jpg')
print(img.shape)

# imgResize=cv2.resize(img,(500,1000))#Width *height
print(img.shape)#height ,width , bgr value
imgCropped=img[0:480,200:480]#height and width



cv2.imshow('Image',imgCropped)
cv2.waitKey(0)
