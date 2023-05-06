import mediapipe as mp
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import time
import numpy

sen=5

run = True

capture=cv2.VideoCapture(0)
detecter=FaceMeshDetector(maxFaces=2)
tl=["a","b","c","d","e"]

run = True

while run:
    success,img=capture.read()
    imgText=numpy.zeros_like(img)    
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

        for i, text in enumerate(tl):
            singleHeight = 20 + int((int(d/sen)*sen)/4)
            scale = 0.5 + (int(d/sen)*sen)/35
            cv2.putText(imgText, text,(50,50+(i*singleHeight)),cv2.FONT_HERSHEY_PLAIN,scale,(237,23,144),2)

    imgStacked = cvzone.stackImages([img,imgText],2,1)
    cv2.imshow('Handsometeachter',imgStacked)
    key=cv2.waitKey(1)

    if key == ord('x'):
        run = False
