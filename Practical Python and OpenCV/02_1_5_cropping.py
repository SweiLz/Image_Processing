import cv2

image = cv2.imread("resource/terminator.jpg")
cv2.imshow("Original", image)

#(y1:y2,x1:x2)
cropped = image[60:222, 453:600]
cv2.imshow("Terminator Face", cropped)
cv2.waitKey(0)