# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_face_mesh = mp.solutions.face_mesh

# # 웹캠, 영상 파일의 경우 이것을 사용하세요.:
# drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# with mp_face_mesh.FaceMesh(
#         max_num_faces=1,
#         refine_landmarks=True,
#         min_detection_confidence=0.5,
#         min_tracking_confidence=0.5) as face_mesh:
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print("웹캠을 찾을 수 없습니다.")
#             # 비디오 파일의 경우 'continue'를 사용하시고, 웹캠에 경우에는 'break'를 사용하세요
#             break

#         # 필요에 따라 성능 향상을 위해 이미지 작성을 불가능함으로 기본 설정합니다.
#         image.flags.writeable = False
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = face_mesh.process(image)

#         # 이미지 위에 얼굴 그물망 주석을 그립니다.
#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         if results.multi_face_landmarks:
#             for face_landmarks in results.multi_face_landmarks:
#                 mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_TESSELATION,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
#                 mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_CONTOURS,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
#                 mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_IRISES,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())
#         # 보기 편하게 이미지를 좌우 반전합니다.
#         cv2.imshow('MediaPipe Face Mesh(Puleugo)', cv2.flip(image, 1))
#         key = cv2.waitKey(1)

#         if key == ord('x'):
#             break
# cap.release()

#++++++++++++++=========================================================================================================================================================

import cv2
import mediapipe as mp
import time


mpfacemesh = mp.solutions.face_mesh
mpdraw = mp.solutions.drawing_utils
fashmesh = mpfacemesh.FaceMesh(max_num_faces=1,refine_landmarks=True)
mpdrawspec=mpdraw.DrawingSpec(color=(0,255,0),thickness=1,circle_radius=1)

run = True

capture=cv2.VideoCapture(0)
pTime = 0



run = True

while run:
    success,img=capture.read()
    results=fashmesh.process(img)
    print(results)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpdraw.draw_landmarks(img, faceLms, mpfacemesh.FACEMESH_CONTOURS,mpdrawspec,mpdrawspec)

        for lm in faceLms.landmark:
            ih,iw,ic=img.shape
            x,y=int(lm.x * iw),int(lm.y * ih)
            print("id:"+str(id),end='')
            print("x:"+str(id),end='')
            print("y:"+str(y))






    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f"FPS : {str(int(fps))}",(400,450),cv2.FONT_HERSHEY_PLAIN,3,(30,255,20),5)

    cv2.imshow('Handsometeachter',img)
    key=cv2.waitKey(1)

    if key == ord('x'):
        run = False
