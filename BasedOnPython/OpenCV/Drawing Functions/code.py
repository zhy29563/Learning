'''
Detailed Description

Drawing functions work with matrices/images of arbitrary depth.
The boundaries of the shapes can be rendered with antialiasing (implemented only for 8-bit images for now).
All the functions include the parameter color that uses an RGB value (that may be constructed with the Scalar
constructor ) for color images and brightness for grayscale images. For color images, the channel ordering
is normally Blue, Green, Red. This is what imshow, imread, and imwrite expect. So, if you form a color using
the Scalar constructor, it should look like:
    Scalar(blue_component,green_component,red_component[,alpha_component])

If you are using your own image rendering and I/O functions, you can use any channel ordering.
The drawing functions process each channel independently and do not depend on the channel order
or even on the used color space. The whole image can be converted from BGR to RGB or to a different
color space using cvtColor .

If a drawn figure is partially or completely outside the image, the drawing functions clip it.
Also, many drawing functions can handle pixel coordinates specified with sub-pixel accuracy.
This means that the coordinates can be passed as fixed-point numbers encoded as integers.
The number of fractional bits is specified by the shift parameter and the real point coordinates
are calculated as Point(x,y)→Point2f(x∗2−shift,y∗2−shift) . This feature is especially effective
when rendering antialiased shapes.

Note
    The functions do not support alpha-transparency when the target image is 4-channel.
    In this case, the color[3] is simply copied to the repainted pixels. Thus, if you want to paint
    semi-transparent shapes, you can paint them in a separate buffer and then blend it with the main image.
'''
import numpy as np
import cv2 as cv
from numpy.core.defchararray import array
###########################################################################################
# 读取图像
###########################################################################################
mat = cv.imread('lena.png')

###########################################################################################
# 绘制带箭头的直线
###########################################################################################
# Draws a arrow segment pointing from the first point to the second one.
# img=cv.arrowedLine(img, pt1, pt2, color[, thickness[, line_type[, shift[, tipLength]]]])
'''
Parameters
    img         Image.
    pt1         The point the arrow starts from.
    pt2         The point the arrow points to.
    color       Line color.
    thickness   Line thickness.
    line_type   Type of the line. See LineTypes
    shift       Number of fractional bits in the point coordinates.
    tipLength   The length of the arrow tip in relation to the arrow length
'''
#  LineTypes
'''
cv.FILLED
cv.LINE_4
    4-connected line

cv.LINE_8
    8-connected line

cv.LINE_AA
    antialiased line
'''
cv.arrowedLine(mat, (10,10), (100,100), (255,0,0), 2)

###########################################################################################
# 绘制圆
###########################################################################################
# img=cv.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
'''
Parameters
    img         Image where the circle is drawn.
    center      Center of the circle.
    radius      Radius of the circle.
    color       Circle color.
    thickness   Thickness of the circle outline, if positive.
                Negative values, like FILLED, mean that a filled circle is to be drawn.
    lineType    Type of the circle boundary. See LineTypes
    shift       Number of fractional bits in the coordinates of the center and in the radius value.
'''
cv.circle(mat, (200,200), 50, (0,255,0), 2)

###########################################################################################
# 绘制带裁剪区域的直线
###########################################################################################
# Clips the line against the image rectangle.
# retval, pt1, pt2=cv.clipLine(imgRect, pt1, pt2)
'''
The function cv::clipLine calculates a part of the line segment that is entirely within the specified
rectangle. it returns false if the line segment is completely outside the rectangle. Otherwise,
it returns true .

Parameters
    imgRect Image rectangle.
    pt1     First line point.
    pt2     Second line point.
'''
retval, pt1, pt2=cv.clipLine((100, 100, 300, 300), (-100,-100), (1000,1000))
print(retval, pt1, pt2)

###########################################################################################
# 绘制轮廓
###########################################################################################
# The function draws contour outlines in the image if thickness≥0 or
# fills the area bounded by the contours if thickness<0 .
# image=cv.drawContours(	image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]	)
'''
Parameters
    image       Destination image.
    contours    All the input contours. Each contour is stored as a point vector.
    contourIdx  Parameter indicating a contour to draw. If it is negative, all the contours are drawn.
    color       Color of the contours.
    thickness   Thickness of lines the contours are drawn with.
                If it is negative (for example, thickness=FILLED ), the contour interiors are drawn.
    lineType    Line connectivity. See LineTypes
    hierarchy   Optional information about hierarchy. 
                It is only needed if you want to draw only some of the contours (see maxLevel ).
    maxLevel    Maximal level for drawn contours.
                If it is 0, only the specified contour is drawn.
                If it is 1, the function draws the contour(s) and all the nested contours.
                If it is 2, the function draws the contours, all the nested contours, all the nested-to-nested contours, and so on.
                This parameter is only taken into account when there is hierarchy available.
    offset      Optional contour shift parameter.
                Shift all the drawn contours by the specified offset=(dx,dy) .
Note
    When thickness=FILLED, the function is designed to handle connected components with holes correctly
    even when no hierarchy date is provided. This is done by analyzing all the outlines together using
    even-odd rule. This may give incorrect results if you have a joint collection of separately retrieved
    contours. In order to solve this problem, you need to call drawContours separately for each sub-group
    of contours, or iterate over the collection using contourIdx parameter.
'''
contour = np.ndarray((4,1,2), np.uint8, np.array([[[0,0]], 
                                         [[100,0]], 
                                         [[100,100]],
                                         [[0,100]]]))
cv.drawContours(mat, [contour], -1, (0,0,255), 2)

cv.imshow('test', mat)
cv.waitKey()
cv.destroyAllWindows()