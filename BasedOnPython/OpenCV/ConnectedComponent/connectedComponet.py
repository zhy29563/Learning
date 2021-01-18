import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import random as rd
import os

def connected_components(img):
    # 二值化
    _, binary = cv.threshold(img, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)

    # 形态学
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)

    # 连通域
    retval, labels = cv.connectedComponents(binary)

    # 使用不同的颜色标记连通域
    colors = []
    for i in range(retval):
        r = rd.randint(0, 256)
        g = rd.randint(0, 256)
        b = rd.randint(0, 256)
        colors.append((b, g, r))

    imgShow = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    w,h = img.shape[:2]
    for i in range(w):
        for j in range(h):
            label = labels[i,j]
            if label == 0:
                continue
            imgShow[i,j,:] = colors[label]

    cv.imshow('Label', imgShow)
        
def connected_components_stat(img):
    # 二值化
    _, binary = cv.threshold(img, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)

    # 形态学
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)

    # 连通域
    retval, labels, stats, centroids = cv.connectedComponentsWithStats(binary)

    imgShow = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    # 使用不同的颜色标记连通域
    colors = []
    for i in range(retval):
        r = rd.randint(0, 256)
        g = rd.randint(0, 256)
        b = rd.randint(0, 256)
        color = (b, g, r)
        colors.append(color)

        # 绘制质心
        x = int(centroids[i][0])
        y = int(centroids[i][1])
        cv.circle(imgShow, (x,y), 5, color, -1)

        # 提取其中矩形的边界
        l = stats[i][cv.CC_STAT_LEFT]
        t = stats[i][cv.CC_STAT_TOP]
        w = stats[i][cv.CC_STAT_WIDTH]
        h = stats[i][cv.CC_STAT_HEIGHT]
        # 绘制矩形
        cv.rectangle(imgShow, (l, t), (l + w,t + h), color, 2)

    cv.imshow('LabelWithStart', imgShow)


if __name__ == "__main__":
    print(os.getcwd ())
    img = cv.imread('rice.png', cv.IMREAD_GRAYSCALE)

    connected_components(img)
    connected_components_stat(img)

    cv.waitKey()
    cv.destroyAllWindows()