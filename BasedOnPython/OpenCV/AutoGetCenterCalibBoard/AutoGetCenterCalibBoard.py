import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

# 读取图像
#imgGray = cv.imread('.\\OpenCV\\CalibrationBoard.bmp', cv.IMREAD_GRAYSCALE)
imgGray = cv.imread('.\\OpenCV\\02.png', cv.IMREAD_GRAYSCALE)
#plt.imshow(imgGray, cmap ='gray')
#plt.show()

# 二值化图像
retval, imgThreshold = cv.threshold(imgGray, 128, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
print(retval)
#plt.imshow(imgThreshold, cmap ='gray')
#plt.show()

# 获取轮廓
'''
轮廓树中的每个值都包含一个四整数数组。在这种情况下，节点的向量标识中的每个部分都附加了一层特殊含义。
层次列表中的每个节点都由四个整数组成。每个数都代表在层次列表中与当前节点由特定关系的另一个节点。
而当前节点之间不存在这样的关系时，数组中的相印元素为-1

索引     含义
0        同级的下一条轮廓
1        同级的前一条轮廓
2        下级的第一个子节点
3        上级父节点

例如：
  0  1  2  3 索引
[ 1 -1 -1 -1]
[ 2  0 -1 -1]
[ 3  1 -1 -1]
'''
# 首先获取最外的轮廓
contours, hierarchy	= cv.findContours(imgThreshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(hierarchy)

# 面积必须大于图像尺寸的一半
imgArea = imgGray * 0.5
area_list = []
area_index_list = []
area_contour_list = []
for i in range(len(contours)):
    area = cv.contourArea(contour=contours[i])
    if(area > imgArea):
        area_list.append(area)
        area_index_list.append(i)
        area_contour_list.append(contours[i])

if(len(area_contour_list) < 1):
    exit

# 根据最小外接矩形的四个顶点都在图像范围内进行筛选
min_rect_countour_list = []
for i in range(len(area_contour_list)):
    rect = cv.minAreaRect(area_contour_list[i])
    points = cv.boxPoints(rect)
    for j in range(len(points)):
        pass








print(contours[0])
imgCountours = imgGray.copy()
imgCountours = cv.cvtColor(imgCountours, cv.COLOR_GRAY2RGB)
cv.drawContours(imgCountours, contours, -1, (0,255,0), 3, cv.LINE_AA)
plt.imshow(imgCountours, cmap ='gray')
plt.show()

# 创建掩模图像
