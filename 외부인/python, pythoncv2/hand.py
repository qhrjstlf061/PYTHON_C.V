# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# # 웹캠, 영상 파일의 경우 이것을 사용하세요.:
# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("카메라를 찾을 수 없습니다.")
#       # 동영상을 불러올 경우는 'continue' 대신 'break'를 사용합니다.
#       continue

#     # 필요에 따라 성능 향상을 위해 이미지 작성을 불가능함으로 기본 설정합니다.
#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image)

#     # 이미지에 손 주석을 그립니다.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             hand_landmarks,
#             mp_hands.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style(),
#             mp_drawing_styles.get_default_hand_connections_style())
#     #보기 편하게 이미지를 좌우 반전합니다.
#     cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
#     key = cv2.waitKey(1)

#     if key == ord('x'):
#         break
# cap.release()


#=========================================================================

import cv2
import mediapipe as mp
import time
import cvzone

mpHands= mp.solutions.hands
hands = mpHands.Hands(max_num_hands=10, min_detection_confidence=0.5,min_tracking_confidence=0.5)
mpDraw =mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
run = True

while run:
  success, img=cap.read()

  results = hands.process(img)

  if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
              for id, lm in enumerate(handLms.landmark):
                    #print(id,lm)
                    h, w, c = img.shape
                    cx, cy=int(lm.x * w), int(lm.y * h)
                    #print(id, cx, cy)
                    
                    if id == 4:
                      #print(id, cx, cy)
                      cv2.circle(img, (cx, cy), 10, (0, 255, 25), cv2.FILLED)   
                    elif id == 8:
                      #print(id,cx,cy)
                      cv2.circle(img, (cx, cy), 10, (0, 255, 25), cv2.FILLED)
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

  cv2.imshow('H.T', cv2.flip(img, 1))
  key = cv2.waitKey(1)





  if key == ord('x'):
    run = False