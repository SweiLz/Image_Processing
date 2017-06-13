import numpy as np
import cv2

image = cv2.imread("resource/terminator.jpg")
cv2.imshow("Original", image)

r = 150.0/image.shape[1]
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image,dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

r = 50.0/image.shape[0]
dim = (int(image.shape[1]*r),50)

resized = cv2.resize(image,dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

def resize(image, width=None, height=None,inter =cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height/float(h)
        dim = (int(w*r), height)
    else:
        r = width/float(w)
        dim = (width, int(h*r))
    resized = cv2.resize(image,dim,interpolation=inter)
    return resized



resized = resize(image, width = 100)
cv2.imshow("Resized (Width) via Function", resized)

resized = resize(image, height = 80)
cv2.imshow("Resized (Height) via Function", resized)

cv2.waitKey(0)