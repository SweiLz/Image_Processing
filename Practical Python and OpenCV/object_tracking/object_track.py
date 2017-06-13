import numpy as np
import cv2

blueLower = np.array([91, 108, 109], dtype="uint8")
blueUpper = np.array([111, 255, 252], dtype="uint8")

cam = cv2.VideoCapture(0)

while True:
    frame = cam.read()[1]
    frameClone = frame.copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue = cv2.inRange(frame, blueLower, blueUpper)
    blue = cv2.GaussianBlur(blue, (3, 3), 0)

    cnts = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

    if len(cnts)>0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frameClone, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Tracking", frameClone)
    cv2.imshow("Binary", blue)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()

