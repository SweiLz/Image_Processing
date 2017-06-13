import numpy as np
import cv2

print("START")
cv2.namedWindow('frame')


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) #set high
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)  #set width


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    edge = cv2.Canny(frame,100,200)

    # Display the resulting frame
    cv2.imshow('frame',edge)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        print("END by user")
        break
    elif key & 0xFF == ord('s'):
        cv2.imwrite('test.jpeg',gray)
        print("Saved")


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()