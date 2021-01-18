import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv



numRow = 1
numCol = 2
plt.figure()

# 原始图像
imgRaw = cv.imread('00.bmp', cv.IMREAD_GRAYSCALE)
plt.subplot(numRow, numCol, 1)
plt.title('Raw')
plt.imshow(imgRaw, cmap ='gray')

#二值化
_, imgBinary = cv.threshold(imgRaw, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
plt.subplot(numRow, numCol, 2)
plt.title('Binary')
plt.imshow(imgBinary, cmap ='gray')

contours, hierarchy	= cv.findContours(imgBinary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv.contourArea(contour)
    if area < 200:
        continue
    moments = cv.moments(contour, False)
    hu_moments = cv.HuMoments(moments)

    print(moments);
    print(hu_moments);

plt.show()