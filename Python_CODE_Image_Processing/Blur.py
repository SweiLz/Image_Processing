import cv2
import numpy as np

from matplotlib import pyplot as plt

print("START")

img = cv2.imread('tu.jpg')

#Blur using 2D convolution
kernel1 = np.ones((5, 5), np.float32) / 25  #create kernel 5x5 and assign '1' and divided by 25
avgImg = cv2.filter2D(img, -1, kernel1)
kernel2 = np.array([[1,2,1],[2,4,2],[1,2,1]])/16  #create custom array
avgImg2 = cv2.filter2D(img,-1,kernel2)

#Blur using OpenCV MedianBlur function by kernel 5x5
median = cv2.medianBlur(img, 5)

#Bilateral Filtering
BilatImg = cv2.bilateralFilter(img, 9, 75, 75)
"""
#show image using opencv imshow
cv2.imshow('Frame', img)
cv2.imshow('Median',median)
cv2.imshow('Average',avgImg)
cv2.imshow('Bilateral Filtering',BilatImg)
"""
cv2.imshow('original',img)
plt.subplot(222), plt.imshow(cv2.cvtColor(avgImg2,cv2.COLOR_BGR2RGB)), plt.title('Averaging2')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB)), plt.title('MedianBlur')
plt.xticks([]), plt.yticks([])
plt.subplot(221), plt.imshow(cv2.cvtColor(avgImg,cv2.COLOR_BGR2RGB)), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(cv2.cvtColor(BilatImg,cv2.COLOR_BGR2RGB)), plt.title('Bilateral Filtering')
plt.xticks([]), plt.yticks([])
plt.show()

#wait any key to continue
cv2.waitKey()
