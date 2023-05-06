import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceMeshModule import FaceMeshDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

startgame = True

detecterh = HandDetector(maxHands=1)
detecterf=FaceMeshDetector()

run =True

ges=" "

while run:
    img = cap.read()
    success, img = cap.read()
    img, faces = detecterf.findFaceMesh(img,draw=False)
    hands, img = detecterh.findHands(img)  # with draw

    if startgame:
        
        cvzone.putTextRect(img, ges,(100, 80),3,3,(237,23,144),(0,0,0),cv2.FONT_HERSHEY_PLAIN,)

        if hands:
            hand = hands[0]
            finger1 = detecterh.fingersUp(hand)
            if finger1 == [1, 1, 1, 1, 1]:
                ges = "dog"
            if finger1 == [1, 1, 1, 0, 0]:
                ges = "gun"
            if finger1 == [0, 1, 1, 0, 0]:
                ges = "V"
            if finger1 == [1, 1, 0, 0, 1]:
                ges = "Yaa"
            if finger1 == [1, 0, 0, 0, 0]:
                ges = "good"
            if finger1 == [1, 0, 0, 0, 1]:
                ges = "promise"
             



    cv2.imshow("Image", img)
    # cv2.imshow("Scaled", imgScaled)



    key = cv2.waitKey(1)

    if key == ord('s'):
        startgame = True
    
    if key == ord('r'):
        startgame = False
    
    if key == ord('x'):
        run = False

        
