#Read Images Video and Webcam
import cv2 

## for image
# img=cv2.imread('Resources/image1.jpg')
# cv2.imshow("Image",img)
# cv2.waitKey(0)
## if we put 1000insted of 0 then it means 1000miliseconds

# #For Video
# cap=cv2.VideoCapture("Resources/video1.mp4")
# while True:
#     success,img=cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

#For Webcam
cap=cv2.VideoCapture(0)
frameWidth=640
frameHeight=480
cap.set(3,frameWidth)#For width
cap.set(4,frameHeight)#For height
cap.set(10,150)#For brightness
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)#For flipping
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
