import numpy as np
import cv2

img = cv2.imread('canvas.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

triangleCount = 0
squareCount = 0
rectangleCount = 0
circleCount = 0


for i in range(0, len(contours)):

    cnt = contours[i]

    cnt = contours[i]
    M = cv2.moments(cnt)

    # Get Center of Object
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.circle(img, (cx, cy), 5, (255, 255, 0), -1)

    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

    if len(approx) > 5:
        circleCount+=1
        cv2.drawContours(img, [cnt], 0, (255,255,0), -1)
        cv2.putText(img,'Circle', (cx, cy -20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),1, cv2.LINE_AA)

    elif len(approx) == 3:
        triangleCount+=1
        cv2.drawContours(img, [cnt], 0,(255,0,255), -1)
        cv2.putText(img, 'Triangle', (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    elif len(approx) == 4:
        # Find ratio to separate square and rectangle
        x, y, w, h = cv2.boundingRect(cnt)
        if float(w) / h == 1:
            squareCount+=1
            cv2.drawContours(img, [cnt], 0, (0,255,0), -1)
            cv2.putText(img, 'Square', (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        else:
            rectangleCount+=1
            cv2.drawContours(img, [cnt], 0,(0,255,255), -1)
            cv2.putText(img, 'Rectangle', (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    # Mark center point
    cv2.circle(img, (cx, cy), 5, (0, 0, 0), -1)
    cv2.putText(img,'('+str(cx)+','+str(cy)+')',(cx,cy+20), cv2.FONT_HERSHEY_SIMPLEX,    0.5,(0,0,255),1,cv2.LINE_AA)

# Show Count Summary
cv2.putText(img,'Circle = '+str(circleCount)+' Triangle = '+str(triangleCount)+' Square = '+str(squareCount)+' Rectangle = '+str(rectangleCount),(np.size(img,1) - 450,np.size(img,0)-20), cv2.FONT_HERSHEY_SIMPLEX,    0.5,(0,0,255),1,cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()