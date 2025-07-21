import cv2
import pyautogui
import mediapipe
capture_hands= mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
camera = cv2.VideoCapture(0)
screen_width,screen_height= pyautogui.size()
x1=x2=y1=y2=0
while True:
    ret, image= camera.read()
    image_height,image_width,_= image.shape
    image= cv2.flip(image,1)
   
    image_rgb= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands= capture_hands.process(image_rgb)
    all_hands= output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks=hand.landmark
            for id,lm in enumerate(one_hand_landmarks):
                x=int(lm.x*image_width)
                y=int(lm.y*image_height)
                # print(x,y)
                if id==8:
                    mouse_x=int(screen_width*x/image_width)
                    mouse_y=int(screen_height*y/image_height)
                    cv2.circle(image,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1=x
                    y1=y
                if id==4:
                    x2=x
                    y2=y
                    cv2.circle(image,(x,y),10,(0,255,255))
        dist=y2-y1
        print(dist) 
        if(dist<40):
            pyautogui.click()
            print("click")
    cv2.imshow("Hand movement video capture",image)
    key= cv2.waitKey(100)
    if key ==27: 
       break
camera.release() 
cv2.destroyAllWindows()