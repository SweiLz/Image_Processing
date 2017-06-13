import numpy as np
import cv2

def nothing(x):
    pass


cap = cv2.VideoCapture(1)

cap.set(3, 640);
cap.set(4, 480);

cv2.namedWindow('Output')
cv2.namedWindow('Trackbars', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Hue_Low', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Saturation_Low', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Value_Low', 'Trackbars', 0, 255, nothing)

cv2.createTrackbar('Hue_High', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Saturation_High', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Value_High', 'Trackbars', 0, 255, nothing)


while(cap.isOpened()):

    ret,img = cap.read()

    # canny = cv2.Canny(img,100,200);
    #
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    #
    # cv2.imshow('threshORG',canny)
    #
    # im2, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    #
    # cv2.imshow('thresh',thresh)
    #
    # cv2.imshow('canny',canny)

    img = cv2.Canny(img,100,60)

    # thresh = cv2.inRange(hsv,[10,100,100],[10,100,100])

    # cv2.imshow('thresh',thresh)




    cv2.imshow('img',img)


    userKey = cv2.waitKey(3)

    if userKey==27:
        break

cv2.destroyAllWindows()
