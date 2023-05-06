# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_holistic = mp.solutions.holistic


# cap = cv2.VideoCapture(0)
# with mp_holistic.Holistic(
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as holistic:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
     
#       continue



#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = holistic.process(image)


#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     mp_drawing.draw_landmarks(
#         image,
#         results.face_landmarks,
#         mp_holistic.FACEMESH_CONTOURS,
#         landmark_drawing_spec=None,
#         connection_drawing_spec=mp_drawing_styles
#         .get_default_face_mesh_contours_style())
#     mp_drawing.draw_landmarks(
#         image,
#         results.pose_landmarks,
#         mp_holistic.POSE_CONNECTIONS,
#         landmark_drawing_spec=mp_drawing_styles
#         .get_default_pose_landmarks_style())

#     cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
#     key = cv2.waitKey(1)

#     if key == ord('x'):
#         break
# cap.release()

#=======================================================

import cv2
import time
import mediapipe as mp
 
cap= cv2.VideoCapture(0)
pTime=0
mppose=mp.solutions.pose
mpdrawstyle=mp.solutions.drawing_styles
mpdraw=mp.solutions.drawing_utils
pose=mppose.Pose()

run=True

while run:
    success,img=cap.read()
    results=pose.process(img)
    
    if results.pose_landmarks:
        mpdraw.draw_landmarks(img,results.pose_landmarks,mppose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            if id<=10:
                cv2.circle(img,(cx,cy),5,(0,0,255),5,cv2.FILLED)
            elif id<=22 and id>10:
                cv2.circle(img,(cx,cy),5,(0,255,0),5,cv2.FILLED)
            elif id<=32 and id>22:
                cv2.circle(img,(cx,cy),5,(255,0,0),5,cv2.FILLED)          
    ctime=time.time()
    fps=1/(ctime-pTime)
    pTime=ctime
    cv2.putText(img, f"FPS : {str(int(fps))}",(400,450),cv2.FONT_HERSHEY_PLAIN,3,(30,255,20),5)
    
    
    
    cv2.imshow('holistic',img)
    key=cv2.waitKey(1)
    if key ==ord('x'):
        run =False
    