import mediapipe as mp
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.HandTrackingModule import HandDetector
import time
import random
import numpy

detecter=FaceMeshDetector(maxFaces=1)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(maxHands=1)
sen=5
tl=["tumb","index","middle","ring"]

success,img=cap.read()
imgText=numpy.zeros_like(img)    
img, faces = detecter.findFaceMesh(img,draw=False)

run=True

while run:
    success, img = cap.read()
    imgText=numpy.zeros_like(img)
    img, faces = detecter.findFaceMesh(img,draw=False)
    hands, img = detector.findHands(img) 
    # imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    # imgScaled = imgScaled[:, 80:480]

    if hands:
        playerMove = None
    hand = hands[0]
    fingers = detector.fingersUp(hand)
    if fingers == [0, 1, 0, 0, 0]:
        playerMove = 1
    if fingers == [1, 1, 1, 1, 1]:
        playerMove = 2
    if fingers == [0, 1, 1, 0, 0]:
        playerMove = 3





    cv2.imshow('Handsometeachter',img)
    key=cv2.waitKey(1)

    if key == ord('x'):
        run = False     


