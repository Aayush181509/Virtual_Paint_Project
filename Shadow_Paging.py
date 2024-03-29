import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [[0,255,84,179,255,188],
            [35,166,68,179,244,255],
            [55,255,25,179,255,138]]
myColorValues = [[51,153,255],
                 [255,0,255],
                 [0,255,0]]
myPoints = []

def findColor(img, myColor,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColor:

        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #cv2.imshow(str(color[0]), mask)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        #cv2.imshow("Image", mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area > 500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 255, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #objCor = (len(approx))
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
while True:
    success,img = cap.read()
    img=cv2.flip(img,1)
    # imgResult = img.copy()
    imgResult = np.zeros_like(img)
    imgResult[:] = 255, 255, 255
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Video",imgResult)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break