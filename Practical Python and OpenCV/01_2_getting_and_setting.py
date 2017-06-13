import cv2

image = cv2.imread("resource/terminator.jpg")
cv2.imshow("Original",image)

(b, g, r) = image[0, 0]
print ("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print ("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

coner = image[0:100, 0:100]
cv2.imshow("Coner", coner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Update", image)
cv2.waitKey(0)