
import mediapipe as mp
import cv2
import time
import cvzone

cap = cv2.VideoCapture(0)
pTime = 0

mpfacemesh = mp.solutions.face_mesh
mpHands= mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7,min_tracking_confidence=0.7)
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(min_detection_confidence=0.7)
mpfacemesh = mp.solutions.face_mesh
fashmesh = mpfacemesh.FaceMesh(max_num_faces=1,refine_landmarks=True)
mpdrawspec=mpDraw.DrawingSpec(color=(0,255,0),thickness=1,circle_radius=1)
fashmesh = mpfacemesh.FaceMesh(max_num_faces=1,refine_landmarks=True)
mpdrawspec=mpDraw.DrawingSpec(color=(0,255,0),thickness=1,circle_radius=1)
mppose=mp.solutions.pose
mpdrawstyle=mp.solutions.drawing_styles
pose=mppose.Pose()

run = True

while run:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    results_hand = hands.process(img)
    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
    results_pose=pose.process(img)
    
    if results_pose.pose_landmarks:
        mpDraw.draw_landmarks(img,results_pose.pose_landmarks,mppose.POSE_CONNECTIONS)
        for id,lm in enumerate(results_pose.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            if id<=10:
                cv2.circle(img,(cx,cy),5,(0,0,255),5,cv2.FILLED)
            elif id<=22 and id>10:
                cv2.circle(img,(cx,cy),5,(0,255,0),5,cv2.FILLED)
            elif id<=32 and id>22:
                cv2.circle(img,(cx,cy),5,(255,0,0),5,cv2.FILLED)          

            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1]),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 5)
    
    if results_hand.multi_hand_landmarks:
            for handLms in results_hand.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                        #print(id,lm)
                        h, w, c = img.shape
                        cx, cy=int(lm.x * w), int(lm.y * h)
                        #print(id, cx, cy)
                        
                        if id == 4:
                        #print(id, cx, cy)
                            cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)   
                        elif id == 8:
                        #print(id,cx,cy)
                            cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
                        elif id == 12:
                        #print(id,cx,cy)
                            cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)                      
                        elif id == 16:
                        #print(id,cx,cy)
                            cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
                        elif id == 20:
                        #print(id,cx,cy)
                            cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)


                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

  
    results_mesh=fashmesh.process(img)
    #print(results)
    if results_mesh.multi_face_landmarks:
        for faceLms in results_mesh.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpfacemesh.FACEMESH_CONTOURS,mpdrawspec,mpdrawspec)
    
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS : {str(int(fps))}",(400,450),cv2.FONT_HERSHEY_PLAIN,3,(30,255,20),5)

    cv2.imshow("handsometeacher", cv2.flip(img,1))
    key = cv2.waitKey(1)

    if key == ord('x'):
        run = False

