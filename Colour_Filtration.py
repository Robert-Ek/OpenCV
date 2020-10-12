import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

# define range of PURPLE color in HSV
lower_red = np.array([153,102,255])
upper_red = np.array([128,0,0])

# loop until break statement is exectured
while True:
    
    # Read webcam image
    ret, frame = cap.read()
    
    # Convert image from RBG/BGR to HSV so we easily filter
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # Use inRange to capture only the values between lower & upper_blue
    mask = cv2.inRange(hsv_img, lower_red, upper_red)

    # Perform Bitwise AND on mask and our original frame to show only red pixels in the normal feed
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame) #display the unaltered feed 
    cv2.imshow('mask', mask) #display the captured
    cv2.imshow('Filtered Color Only', res)
    if cv2.waitKey(1) == 13: #Press the the Enter Key
        break
        
cap.release() #stop capturing the video feed
cv2.destroyAllWindows() #destroy all remaining openCV windows
