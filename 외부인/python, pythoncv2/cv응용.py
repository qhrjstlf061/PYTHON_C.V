import mediapipe as mp
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import time
import numpy


run = True

capture=cv2.VideoCapture(0)
detecter=FaceMeshDetector(maxFaces=2)
pTime = 0
run = True

while run:
    success,img=capture.read()
    img, faces = detecter.findFaceMesh(img,draw=False)

    if faces:
        face=faces[0]
        pointRight=face[145]
        pointLeft=face[374]

        cv2.line(img,pointLeft,pointRight,(237,23,144),2)
        cv2.circle(img,pointRight,5,(237,23,144),cv2.FILLED)
        cv2.circle(img,pointLeft,5,(237,23,144),cv2.FILLED)

        w, _ = detecter.findDistance(pointLeft,pointRight)

        W=6.3
        f=574

        # f=(w*d)/W
        # print(f)
        d=(W*f)/w
        cvzone.putTextRect(img, f"depth:{int(d)}cm",(face[10][0] - 100, face[10][1]-50),3,3,(237,23,144),(0,0,0),cv2.FONT_HERSHEY_PLAIN,)


    cv2.imshow('Handsometeachter',img)
    key=cv2.waitKey(1)

    if key == ord('x'):
        run = False
