import numpy as np
import cv2 as cv

winname = 'test'
#cv.namedWindow(winname, cv.WINDOW_GUI_EXPANDED | cv.WINDOW_NORMAL | cv.WINDOW_KEEPRATIO)
mat = cv.imread('ROtatedRect.png', cv.IMREAD_GRAYSCALE)

_, binary = cv.threshold(mat, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
imgColor = cv.cvtColor(mat, cv.COLOR_GRAY2BGR)
cv.drawContours(imgColor, contours, -1, (255,0,0), 2)
print(type(contours))
print(type(contours[0]))
print(contours[0].shape)
print(type(contours[0][0]))
print(type(contours[0][0][0]))
print(type(contours[0][0][0][0]))
#cv.imshow(winname, imgColor)
for contour in contours:
    rect   = cv.minAreaRect(contour)
    points = cv.boxPoints(rect)
    matrix = cv.getRotationMatrix2D(rect[0], rect[2], 1)
    dst    = cv.warpAffine(mat, matrix, mat.shape)
    #cv.imshow('dst', dst)


cv.waitKey()
cv.destroyAllWindows()