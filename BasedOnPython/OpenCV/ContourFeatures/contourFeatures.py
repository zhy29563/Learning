import numpy as np
import cv2 as cv
import math

def arcLength(contours, centers, img):
    for i in range(len(contours)):
        length = cv.arcLength(contours[i], True)
        cv.putText(img, str(i) + ':' + str(length), centers[i], cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv.imshow("Length", img)

def boundingRect(contours, img):
    for i in range(len(contours)):
        rect = cv.boundingRect(contours[i])
        print(rect)
        #cv.putText(img, str(i) + ':' + str(length), centers[i], cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        cv.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0,255, 0), 2)
    cv.imshow("BoundingRect", img)

def contourArea(contours, centers, img):
    for i in range(len(contours)):
        area = cv.contourArea(contours[i])
        cv.putText(img, str(i) + ':' + str(area), centers[i], cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv.imshow("Area", img)

def convexHull (contours, img):
    cv.drawContours(img, contours, -1, (0,0,255), 6)
    for i in range(len(contours)):
        # 计算凸包
        hull_point = cv.convexHull (contours[i])
        for j in range(hull_point.shape[0]):
            cv.line(img, tuple(hull_point[j, 0]), tuple(hull_point[(j + 1) % hull_point.shape[0], 0]), (0,255,0), 2)
        
        # 需要使用索引输出，否则convexityDefects报错
        hull_index = cv.convexHull (contours[i], returnPoints=False)
        defects = cv.convexityDefects(contours[i], hull_index)
        cnt = 0
        for i in range(defects.shape[0]):  # calculate the angle
            print(defects[i])
            s, e, f, d = defects[i][0]
            
            start = tuple(contours[i][s][0])
            end = tuple(contours[i][e][0])
            far = tuple(contours[i][f][0])
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
            if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                cnt += 1
                cv.circle(img, far, 8, [211, 84, 0], -1)
    cv.imshow("ConvexHull", img)

def centroid(contours):
    center_of_mass_arr = []
    for contour in contours:
        m = cv.moments(contour)
        x = m['m10'] / m['m00']
        y = m['m01'] / m['m00']
        center = (int(x), int(y))
        center_of_mass_arr.append(center)

    return center_of_mass_arr

if __name__ == "__main__":
    src = cv.imread('SelectShape.png', cv.IMREAD_GRAYSCALE)
    #cv.imshow("Src", img)
    # 二值化
    _, binary = cv.threshold(src, 0, 255, cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    # 轮廓查找
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #print(hierarchy)
    # 显示图像
    img = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    
    centers = centroid(contours)
    #arcLength(contours, centers, img)
    #boundingRect(contours, img)
    #contourArea(contours, centers, img)
    convexHull (contours, img)

    cv.waitKey()
    cv.destroyAllWindows()