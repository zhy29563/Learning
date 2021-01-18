import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

numRow = 3
numCol = 4

"""
retval, dst= cv.threshold(src, thresh, maxval, type[, dst])

Parameters
    src
        输入图像(支持多通道, 8位或32位深度浮点数图像).
    dst
        输出图像，尺寸、类型、通道与输入图像相同
    thresh
        使用的阈值
    maxval
        二值化类型为 THRESH_BINARY 与 THRESH_BINARY_INV 时，提取部分的像素值，一般为255
    type
        阈值类型
        THRESH_BINARY：像素值大于给定阈值的设置为maxvalue, 小于等于给定阈值的灰度值保持不变
        THRESH_BINARY_INV：像素值小于等于给定阈值的设置为maxvalue, 大于给定阈值的灰度值保持不变
        THRESH_TRUNC：像素值大于给定阈值的设置为thresh, 小于等于给定阈值的灰度值保持不变
        THRESH_TOZERO：像素值大于给定阈值的设置为0, 小于等于给定阈值的灰度值保持不变
        THRESH_TOZERO_INV：像素值小于等于给定阈值的设置为0, 大于给定阈值的灰度值保持不变

        THRESH_OTSU与THRESH_TRIANGLE可与上面五种方式组合使用，此时的thres通过算法自动进行选择
        THRESH_OTSU：大津法
            参考：https://blog.csdn.net/fangyan90617/article/details/100192100
            1. 计算出图像的直方图
            2. 遍历所有可能的阈值，然后对每个阈值计算 
                小于等于阈值的像素数量 * 小于等于阈值的方差 + 大于阈值的像素数量 * 大于阈值的方差
            3. 取上式的结果最小的阈值作为最终的阈值
        THRESH_TRIANGLE：三角形算法
            参考：https://blog.csdn.net/jia20003/article/details/53954092
            三角法求阈值最早见于Zack的论文《Automatic measurement of sister chromatid exchange frequency》
            主要是用于染色体的研究，该方法是使用直方图数据，基于纯几何方法来寻找最佳阈值，它的成立条件是假设直方
            图最大波峰在靠近最亮的一侧，然后通过三角形求得最大直线距离，根据最大直线距离对应的直方图灰度等级即为
            分割阈值
            1. 图像转灰度
            2. 计算图像灰度直方图
            3. 寻找直方图中两侧边界
            4. 寻找直方图最大值
            5. 检测是否最大波峰在亮的一侧，否则翻转
            6. 计算阈值得到阈值T，如果翻转则255-T
Returns
    如果使用大津法或三角形算法，返回计算得到的阈值

说明：
    The function applies fixed-level thresholding to a multiple-channel array. 
    The function is typically used to get a bi-level (binary) image out of a grayscale
     image ( compare could be also used for this purpose) or for removing a noise, that
      is, filtering out pixels with too small or too large values. There are several 
      types of thresholding supported by the function. They are determined by type parameter.

Also, the special values THRESH_OTSU or THRESH_TRIANGLE may be combined with one of the above
 values. In these cases, the function determines the optimal threshold value using the Otsu's
  or Triangle algorithm and uses it instead of the specified thresh.
"""

fig = plt.figure()
fig.suptitle("Threshold Demo")
imgRaw = np.arange(start=0, stop=256, step=1, dtype=np.uint8).reshape(16, 16)

plt.subplot(numRow, numCol, 1)
plt.title('Raw:Size=16*16, Value = 0-255,')
plt.imshow(imgRaw, cmap ='gray', vmin=0, vmax=255)

"""
Binary:

"""
threshold = 128
maxvalue = 255
_, imgBinary = cv.threshold(imgRaw, threshold, maxvalue, cv.THRESH_BINARY)
plt.subplot(numRow, numCol, 2)
plt.title('Binary:Thres={}'.format(threshold))
plt.imshow(imgBinary, cmap ='gray',vmin=0, vmax=255)

_, imgBinaryInv = cv.threshold(imgRaw, threshold, maxvalue, cv.THRESH_BINARY_INV)
plt.subplot(numRow, numCol, 3)
plt.title('BinaryInv:Thres={}'.format(threshold))
plt.imshow(imgBinaryInv, cmap ='gray',vmin=0, vmax=255)

_, imgTrunc = cv.threshold(imgRaw, threshold, maxvalue, cv.THRESH_TRUNC)
plt.subplot(numRow, numCol, 4)
plt.title('Trunc:Thres={}'.format(threshold))
plt.imshow(imgTrunc, cmap ='gray',vmin=0, vmax=255)

_, imgTozero = cv.threshold(imgRaw, threshold, maxvalue, cv.THRESH_TOZERO)
plt.subplot(numRow, numCol, 5)
plt.title('Tozero:Thres={}'.format(threshold))
plt.imshow(imgTozero, cmap ='gray',vmin=0, vmax=255)

_, imgTozeroInv = cv.threshold(imgRaw, threshold, maxvalue, cv.THRESH_TOZERO_INV)
plt.subplot(numRow, numCol, 6)
plt.title('TozeroInv:Thres={}'.format(threshold))
plt.imshow(imgTozeroInv, cmap ='gray',vmin=0, vmax=255)

# 没搞明白这个是干啥用的，thres设置为255显示原图，其余输出0
_, imgMask = cv.threshold(imgRaw, 255, maxvalue, cv.THRESH_MASK)
plt.subplot(numRow, numCol, 7)
plt.title('Mask:Thres={}'.format(threshold))
plt.imshow(imgMask, cmap ='gray',vmin=0, vmax=255)

_, imgOtsu = cv.threshold(imgRaw, 2, maxvalue, cv.THRESH_BINARY | cv.THRESH_OTSU)
plt.subplot(numRow, numCol, 8)
plt.title('OTSU:InThres={},OutThres={}'.format(2, _))
plt.imshow(imgOtsu, cmap ='gray',vmin=0, vmax=255)

_, imgTriangle = cv.threshold(imgRaw, 2, maxvalue, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
plt.subplot(numRow, numCol, 9)
plt.title('Triangle:InThres={},OutThres={}'.format(2, _))
plt.imshow(imgTriangle, cmap ='gray',vmin=0, vmax=255)

# 自适应阈值
"""
dst = cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])
参数
    src
        8位单通道图像
    dst
        输出图像，与输入图像相同的尺寸与类型
    maxValue
        选择的像素被设置的值
    adaptiveMethod
        自适应阈值选择的方法。ADAPTIVE_THRESH_MEAN_C 与 ADAPTIVE_THRESH_GAUSSIAN_C
        两种方法都是逐个像素地计算自适应阈值T，方法通过计算每个像素位置周围的blockSize*blockSize区域
        的加权平均值然后减去常数C。不同之处在于：
        ADAPTIVE_THRESH_MEAN_C 权值是相等的
        ADAPTIVE_THRESH_GAUSSIAN_C 权值是根据点到中心点的距离通过高斯方程得到
    thresholdTyp
        THRESH_BINARY
        THRESH_BINARY_INV
    blockSize
        邻域尺寸，奇数邻域
    C
        常量
"""

imgAdaptiveMeanBinary = cv.adaptiveThreshold(imgRaw, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 0)
plt.subplot(numRow, numCol, 10)
plt.title('AdaptiveMeanBinary:Size=5')
plt.imshow(imgAdaptiveMeanBinary, cmap ='gray',vmin=0, vmax=255)

imgAdaptiveGaussBinary = cv.adaptiveThreshold(imgRaw, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 0)
plt.subplot(numRow, numCol, 11)
plt.title('AdaptiveGaussBinary:Size=5')
plt.imshow(imgAdaptiveGaussBinary, cmap ='gray',vmin=0, vmax=255)

plt.show()
