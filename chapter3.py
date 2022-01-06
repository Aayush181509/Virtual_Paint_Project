# Crop and Resize
import cv2
import numpy as np

img=cv2.imread('Resources/image1.jpg')
print(img.shape)

imgResize=cv2.resize(img,(500,1000))#Width *height
print(imgResize.shape)


# cv2.imshow('Image',imgResize)
cv2.waitKey(0)
