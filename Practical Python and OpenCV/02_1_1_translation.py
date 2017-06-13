import numpy as np
import cv2

image = cv2.imread("resource/terminator.jpg")
cv2.imshow("Original", image)

M = np.float32([[1, 0, 125], [0, 1, 150]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right",shifted)

M = np.float32([[1, 0, -150], [0, 1, -190]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left",shifted)

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

shifted = translate(image, 0, 100)
cv2.imshow("Shifted Down",shifted)
cv2.waitKey(0)