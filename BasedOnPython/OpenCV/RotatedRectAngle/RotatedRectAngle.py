import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import math

#***** 求两点间距离*****
def getDist_P2P(Point0,PointA):
    distance=math.pow((Point0[0]-PointA[0]),2) + math.pow((Point0[1]-PointA[1]),2)
    distance=math.sqrt(distance)
    return distance
 
 

imgRaw = cv.imread('.\\OpenCV\\0000.png', cv.IMREAD_GRAYSCALE)


_, imgThres = cv.threshold(imgRaw, 128, 255, cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(imgThres, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

imgColor = cv.cvtColor(imgRaw, cv.COLOR_GRAY2RGB)
for contour in contours:
    
    rect = cv.minAreaRect(contour)
    print(rect)

    points = cv.boxPoints(rect)
    dist1 = getDist_P2P(points[0], points[1])
    dist2 = getDist_P2P(points[1], points[2])

    rotation = 0
    if dist1 >= dist2:
        rotation = math.atan2(points[0][1] - points[1][1], points[0][0] - points[1][0])
    else:
        rotation = math.atan2(points[2][1] - points[1][1], points[2][0] - points[1][0])

    while rotation > math.pi * 0.5:
            rotation -= math.pi
    while rotation < math.pi * -0.5:
            rotation += math.pi
    cv.putText(imgColor, 
               'A:{:.3f}'.format(math.degrees(rotation)), 
               ((int)(rect[0][0]), (int)(rect[0][1])), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    


cv.drawContours(imgColor, contours, -1, (0,255,255), 2)
plt.imshow(imgColor)
plt.show()