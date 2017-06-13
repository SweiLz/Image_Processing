import cv2
import numpy as np

from matplotlib import pyplot as plt

print("START")

img = cv2.imread('TU.jpg')

kernel = np.array([[1,1,1],[1,-9,1],[1,1,1]])  #kernel for point detect
dst = cv2.filter2D(img,-1,kernel)

cannyMat = cv2.Canny(img,100,200)


#show Image using plot
plt.subplot(221), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)), plt.title('Apply Kernel')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(cv2.cvtColor(cannyMat,cv2.COLOR_GRAY2RGB)), plt.title('Canny Edge')
plt.xticks([]), plt.yticks([])
plt.show()

#wait any key to continue
cv2.waitKey()
