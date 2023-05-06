
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
run = True

capture=cv2.VideoCapture(0)
pTime = 0
run = True
detector = HandDetector(maxHands=1)

while run:
    success,img=capture.read()

    hands, img = detector.findHands(img)








    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f"FPS : {str(int(fps))}",(400,450),cv2.FONT_HERSHEY_PLAIN,3,(30,255,20),5)

    cv2.imshow('Handsometeachter',img)
    key=cv2.waitKey(1)

    if key == ord('x'):
        run = False