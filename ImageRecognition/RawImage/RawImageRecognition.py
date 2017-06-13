import cv2
import numpy as np
import math



img = cv2.imread('IMG_3556.JPG')
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)





cv2.imshow('Mask',img_grey)
cv2.imshow('Output Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()