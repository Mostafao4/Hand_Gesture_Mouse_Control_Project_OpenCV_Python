import cv2
import pyautogui
import mediapipe
 

camera = cv2.VideoCapture(0)
while True:
    ret, image= camera.read()
    cv2.imshow("Hand movement video capture",image)
    key= cv2.waitKey(100)
    
    if key ==27: 
       break
   
camera.release() 
cv2.destroyAllWindows()