import cv2
import numpy as np

from matplotlib import pyplot as plt

print("START")
1
img = cv2.imread('car.jpg')

k = 1
GauImg = cv2.GaussianBlur(img,(5,5),3)
UnsharpImg = cv2.addWeighted(img,k+1,GauImg,-k,0)
k=4.5
HighBootImg = cv2.addWeighted(img,k+1,GauImg,-k,0)





#show Image using plot
plt.subplot(221), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(cv2.cvtColor(GauImg,cv2.COLOR_BGR2RGB)), plt.title('Gau')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(cv2.cvtColor(UnsharpImg,cv2.COLOR_BGR2RGB)), plt.title('UnSharpMasking')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(cv2.cvtColor(HighBootImg,cv2.COLOR_BGR2RGB)), plt.title('HighBoots')
plt.xticks([]), plt.yticks([])
plt.show()

#wait any key to continue
cv2.waitKey()
