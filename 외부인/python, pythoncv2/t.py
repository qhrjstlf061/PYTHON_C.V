import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

run=True


while run:
    imgBG = cv2.imread("BG - Copy.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    hands, img = detector.findHands(imgScaled) 
    
    cv2.imshow("BG", imgScaled)
    key = cv2.waitKey(1)

    if key == ord('x'):
        run = False  