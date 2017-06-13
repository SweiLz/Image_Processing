import cv2

def nothing(x):
    pass

cv2.namedWindow('Color Range',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('H_Min','Color Range',0,255,nothing)
cv2.createTrackbar('S_Min','Color Range',0,255,nothing)
cv2.createTrackbar('V_Min','Color Range',31,255,nothing)
cv2.createTrackbar('H_Max','Color Range',255,255,nothing)
cv2.createTrackbar('S_Max','Color Range',62,255,nothing)
cv2.createTrackbar('V_Max','Color Range',210,255,nothing)

img = cv2.imread('IMG_3558.JPG')
img = cv2.resize(img,None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)

while True:

    H_Min = cv2.getTrackbarPos('H_Min', 'Color Range')
    S_Min = cv2.getTrackbarPos('S_Min', 'Color Range')
    V_Min = cv2.getTrackbarPos('V_Min', 'Color Range')
    H_Max = cv2.getTrackbarPos('H_Max', 'Color Range')
    S_Max = cv2.getTrackbarPos('S_Max', 'Color Range')
    V_Max = cv2.getTrackbarPos('V_Max', 'Color Range')

    img_hsv = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, (H_Min, S_Min, V_Min), (H_Max, S_Max, V_Max))

    img_out = cv2.bitwise_and(img.copy(), img.copy(), mask=mask)
    cv2.imshow('Output Image', img_out)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()