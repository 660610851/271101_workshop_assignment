#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = ""
all = ""
count = ""
fin = ""
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cx8 = cx
                if id == 7:
                    id7 = int(id)
                    cx7 = cx
                if id == 12:
                    id12 = int(id)
                    cx12 = cx
                if id == 11:
                    id11 = int(id)
                    cx11 = cx
                if id == 16:
                    id16 = int(id)
                    cx16 = cx
                if id == 15:
                    id15 = int(id)
                    cx15 = cx
                if id == 20:
                    id20 = int(id)
                    cx20 = cx
                if id == 19:
                    id19 = int(id)
                    cx19 =cx
            
            if cx4 > cx3:
                Nfing = "Thumb"
            else:
                Nfing = "No finger"
            if  cx8 > cx7:
                Nfing = "Index"
            if cx12 > cx11:
                Nfing = "Middle"
            if cx16 > cx15:
                Nfing = "Ring"
            if cx20 > cx19:
                Nfing = "Pinky "

                
            
            
            if(cx4 > cx3)and ( cx8 > cx7 )and ( cx12 > cx11)and  (cx16 > cx15)and (cx20 > cx19):
                Nfing = ""
            if (cx4 > cx3)and ( cx8 > cx7 )and ( cx12 > cx11)and  (cx16 > cx15)and (cx20 > cx19):
                all = "Pinky"
            else :
                all = ""
            
            if (cx4 > cx3) and ( cx8 > cx7 ):
                count = "Thumb Index"
            else:
                count = ""
            if (cx4 > cx3)and ( cx8 > cx7 )and ( cx12 > cx11):
                count = ""
            else:
                count = ""
            if (cx4 > cx3)and ( cx8 > cx7 )and ( cx12 > cx11)and  (cx16 > cx15):
                fin = ""
            if (cx4 > cx3)and ( cx8 > cx7 )and ( cx12 > cx11)and  (cx16 > cx15)and (cx20 > cx19):
                fin = "Thumb Index Middle Ring "
            else:
                fin = ""
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(str(Nfing)), (225, 415), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.putText(img, str(str(all)), (225, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.putText(img, str(str(count)), (10, 415), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.putText(img, str(str(fin)), (10, 415), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    fps = "Best"; #Frame rate per second
    cv2.putText(img, str(str(fps)), (70, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()