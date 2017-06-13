import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg',0)

img_float32 = np.float32(img)

dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows/2 , cols/2     # center


# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
radius = 100

# mask[crow-range:crow+range, ccol-range:ccol+range] = 1
radius = 70

circle= np.ogrid[-radius:radius,-radius:radius]
mask[crow-radius:crow+radius,rows-radius:rows+radius]= 1

# 0 0 0 0 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 0 0 0 0


# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(211),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(img_back, cmap = 'gray')
plt.title('Low Pass Filtered'), plt.xticks([]), plt.yticks([])

plt.show()