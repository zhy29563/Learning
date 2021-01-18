import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

numRow = 3
numCol = 6
plt.figure()

# 原始图
imgRaw = cv.imread('00.png', cv.IMREAD_GRAYSCALE)
plt.subplot(numRow, numCol, 1)
plt.title('Raw')
plt.imshow(imgRaw, cmap ='gray')

#二值化
_, imgBinary = cv.threshold(imgRaw, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
plt.subplot(numRow, numCol, 2)
plt.title('Binary')
plt.imshow(imgBinary, cmap ='gray')

# 膨胀
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
dst = cv.dilate(imgBinary, kernel, iterations=2)
plt.subplot(numRow, numCol, 3)
plt.title('Dilate_5_5_RECT')
plt.imshow(dst, cmap ='gray')

kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))
dst = cv.dilate(imgBinary, kernel, iterations=2)
plt.subplot(numRow, numCol, 4)
plt.title('Dilate_5_5_CROSS')
plt.imshow(dst, cmap ='gray')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
dst = cv.dilate(imgBinary, kernel, iterations=2)
plt.subplot(numRow, numCol, 5)
plt.title('Dilate_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

# 腐蚀
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
dst = cv.erode(imgBinary, kernel, iterations=2)
plt.subplot(numRow, numCol, 6)
plt.title('Erode_5_5_RECT')
plt.imshow(dst, cmap ='gray')

kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))
dst = cv.erode(imgBinary, kernel, iterations=2)
plt.subplot(numRow, numCol, 7)
plt.title('Erode_5_5_CROSS')
plt.imshow(dst, cmap ='gray')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
dst = cv.erode(imgBinary, kernel, iterations=2)
plt.subplot(numRow, numCol, 8)
plt.title('Erode_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

# 通用
dst = cv.morphologyEx(imgBinary, cv.MORPH_ERODE, kernel, iterations=2)
plt.subplot(numRow, numCol, 9)
plt.title('Ex_Erode_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

dst = cv.morphologyEx(imgBinary, cv.MORPH_DILATE, kernel, iterations=2)
plt.subplot(numRow, numCol, 10)
plt.title('Ex_DILATE_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

dst = cv.morphologyEx(imgBinary, cv.MORPH_OPEN, kernel, iterations=2)
plt.subplot(numRow, numCol, 11)
plt.title('Ex_Open_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

dst = cv.morphologyEx(imgBinary, cv.MORPH_CLOSE, kernel, iterations=2)
plt.subplot(numRow, numCol, 12)
plt.title('Ex_Close_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

dst = cv.morphologyEx(imgBinary, cv.MORPH_GRADIENT, kernel, iterations=2)
plt.subplot(numRow, numCol, 13)
plt.title('Ex_GRADIENT_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))
dst = cv.morphologyEx(imgBinary, cv.MORPH_TOPHAT, kernel, iterations=2)
plt.subplot(numRow, numCol, 14)
plt.title('Ex_TOPHAT_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')


dst = cv.morphologyEx(imgBinary, cv.MORPH_BLACKHAT, kernel, iterations=2)
plt.subplot(numRow, numCol, 15)
plt.title('Ex_BLACKHAT_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')


dst = cv.morphologyEx(imgBinary, cv.MORPH_HITMISS, kernel, iterations=2)
plt.subplot(numRow, numCol, 16)
plt.title('Ex_HITMISS_5_5_ELLIPSE')
plt.imshow(dst, cmap ='gray')

plt.show()