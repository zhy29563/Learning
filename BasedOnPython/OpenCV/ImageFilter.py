import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

'''
Enumerations
    enum cv::MorphShapes
    {
        cv::MORPH_RECT = 0,
        cv::MORPH_CROSS = 1,
        cv::MORPH_ELLIPSE = 2
    }

    enum cv::MorphTypes
    {
        cv::MORPH_ERODE = 0,        erode
        cv::MORPH_DILATE = 1,       dilate
        cv::MORPH_OPEN = 2,         dilate(erode(src,element))
        cv::MORPH_CLOSE = 3,        erode(dilate(src,element))
        cv::MORPH_GRADIENT = 4,     dilate(src,element)−erode(src,element)
        cv::MORPH_TOPHAT = 5,       src−open(src,element)
        cv::MORPH_BLACKHAT = 6,     close(src,element)−src
        cv::MORPH_HITMISS = 7       
    }

    enum cv::SpecialFilter { cv::FILTER_SCHARR = -1 }

Detailed Description
    Functions and classes described in this section are used to perform various linear or
non-linear filtering operations on 2D images. It means that for each pixel location (x,y)
in the source image, its neighborhood is considered and used to compute the response. In
case of a linear filter, it is a weighted sum of pixel values. In case of morphological
operations, it is the minimum or maximum values, and so on. The computed response is stored
in the destination image at the same location (x,y). It means that the output image will
be of the same size as the input image. Normally, the functions support multi-channel arrays,
in which case every channel is processed independently. Therefore, the output image will
also have the same number of channels as the input one.

    Another common feature of the functions and classes described in this section is that,
unlike simple arithmetic functions, they need to extrapolate values of some non-existing pixels.
For example, if you want to smooth an image using a Gaussian 3×3 filter, then, when processing
the left-most pixels in each row, you need pixels to the left of them, that is, outside of the
image. You can let these pixels be the same as the left-most image pixels, or assume that
all the non-existing pixels are zeros, and so on. OpenCV enables you to specify the
extrapolation method.

Depth combinations
    Input depth     Output depth
    CV_8U           -1/CV_16S/CV_32F/CV_64F
    CV_16U/CV_16S   -1/CV_32F/CV_64F
    CV_32F          -1/CV_32F/CV_64F
    CV_64F          -1/CV_64F
'''

numRow = 2
numCol = 3
plt.figure()

# 原始图像
imgRaw = cv.imread('.\\OpenCV\\Lena.png', cv.IMREAD_GRAYSCALE)
plt.subplot(numRow, numCol, 1)
plt.title('Raw')
plt.imshow(imgRaw, cmap ='gray')

'''
线性滤波
'''
# 均值滤波
# 滤波核的值都为1，且进行了归一化
# dst=cv.blur(src, ksize[, dst[, anchor[, borderType]]])
'''
src
    input image; it can have any number of channels, which are processed independently,
     but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst
    output image of the same size and type as src.
ksize
    blurring kernel size.
anchor
    anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.
borderType
    border mode used to extrapolate pixels outside of the image
'''
# 目标图像中的每个像素值都是源图像中相应位置的固定邻域像素的平均值
imgBlur = cv.blur(imgRaw, (5,5))
plt.subplot(numRow, numCol, 2)
plt.title('Blur')
plt.imshow(imgBlur, cmap ='gray', vmin=0, vmax=255)

# 高斯滤波
# dst=cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
'''
'''
imgGaussianBlur = cv.GaussianBlur(imgRaw, (5,5), 100)
plt.subplot(numRow, numCol, 3)
plt.title('GaussianBlur')
plt.imshow(imgGaussianBlur, cmap ='gray', vmin=0, vmax=255)

# 方框滤波
# 方框滤波核的形状是矩形，且核的所有元素相等。
# dst=cv.boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]])
'''
src
    input image.
dst
    output image of the same size and type as src.
ddepth
    the output image depth (-1 to use src.depth()).
ksize
    blurring kernel size.
anchor
    anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.
normalize
    flag, specifying whether the kernel is normalized by its area or not.
borderType
    border mode used to extrapolate pixels outside of the image
'''
#
# cv.blur与cv.boxFilter区别与联系
#   cv.blur是cv.boxFilter的归一化形式
#   由于cv.boxFilter没有归一化，因此可以改变像素值的深度
imgBoxFilter = cv.boxFilter(imgRaw, -1, (5,5))
plt.subplot(numRow, numCol, 4)
plt.title('BoxFilter')
plt.imshow(imgBoxFilter, cmap ='gray', vmin=0, vmax=255)

'''
非线性滤波
'''
# 中值滤波
# dst=cv.medianBlur(src, ksize[, dst])
imgMedianBlur = cv.medianBlur(imgRaw, 5)
plt.subplot(numRow, numCol, 5)
plt.title('MedianBlur')
plt.imshow(imgMedianBlur, cmap ='gray', vmin=0, vmax=255)


# 双边滤波
# dst=cv.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
'''
src
    Source 8-bit or floating-point, 1-channel or 3-channel image.
dst
    Destination image of the same size and type as src .
d
    Diameter of each pixel neighborhood that is used during filtering.
    If it is non-positive, it is computed from sigmaSpace.
sigmaColor
    Filter sigma in the color space. A larger value of the parameter means that
    farther colors within the pixel neighborhood (see sigmaSpace) will be mixed
    together, resulting in larger areas of semi-equal color.
sigmaSpace
    Filter sigma in the coordinate space. A larger value of the parameter means
    that farther pixels will influence each other as long as their colors are
    close enough (see sigmaColor ). When d>0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is proportional to sigmaSpace.
borderType
    border mode used to extrapolate pixels outside of the image
'''
# 由于高斯模糊的过程中是减缓像素在空间上的变化，因此与邻域的关系紧密，而随机噪声在图像噪声在图像间
# 变化幅度又会非常的大。基于这种前提高斯平滑很好的减弱了噪声并保留了小信号。不幸的是，这种方式破坏
# 了边缘信息，最中结果是高斯模糊把边缘也模糊了。
# 相似于高斯平滑，双边滤波对每个像素及其邻域内的像素进行了加权平均。其权重由两个部分组成，第一部分
# 同高斯平滑；第二部分也是高斯权重，不同的是它不是基于空间距离而是色彩强度差计算而来，在多通道图像
# 上强度差由各分量的加权累加代替。

# 滤波核的大小d对算法的效率有很大影响，通常在视频处理时不大于5，但在非实时应用方面可放大9.也可以设
# 置为-1，函数将进行自动选择。

# 
# 实际情况中，通常将sigmaColor与sigmaSpace都设置为2. 较小的sigma值(<10)效果不明显；较大的sigma
# 值(>150)会对图像产生非常显著的影响，使图像有一种卡通效果

# 不支持按位置换

imgBilateralFilter = cv.bilateralFilter(imgRaw, 5, 75,75)
plt.subplot(numRow, numCol, 6)
plt.title('BilateralFilter')
plt.imshow(imgBilateralFilter, cmap ='gray', vmin=0, vmax=255)

plt.show()