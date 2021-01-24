from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
from math import atan2, cos, sin, sqrt, pi


def drawAxis(img, p_, q_, colour, scale):
    p = list(p_)
    q = list(q_)

    angle = atan2(p[1] - q[1], p[0] - q[0])  # angle in radians
    hypotenuse = sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))
    # Here we lengthen the arrow by a factor of scale
    q[0] = p[0] - scale * hypotenuse * cos(angle)
    q[1] = p[1] - scale * hypotenuse * sin(angle)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv.LINE_AA)
    # create the arrow hooks
    p[0] = q[0] + 9 * cos(angle + pi / 4)
    p[1] = q[1] + 9 * sin(angle + pi / 4)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv.LINE_AA)
    p[0] = q[0] + 9 * cos(angle - pi / 4)
    p[1] = q[1] + 9 * sin(angle - pi / 4)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv.LINE_AA)


def getOrientation(pts, img):
    '''
    pts:单个轮廓
    img:彩色图像，用于显示
    '''
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)
    for i in range(data_pts.shape[0]):
        data_pts[i, 0] = pts[i, 0, 0]
        data_pts[i, 1] = pts[i, 0, 1]
    # Perform PCA analysis
    mean = np.empty((0))
    mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)
    # Store the center of the object
    cntr = (int(mean[0, 0]), int(mean[0, 1]))

    cv.circle(img, cntr, 3, (255, 0, 255), 2)
    p1 = (cntr[0] + 0.02 * eigenvectors[0, 0] * eigenvalues[0, 0], cntr[1] + 0.02 * eigenvectors[0, 1] * eigenvalues[0, 0])
    p2 = (cntr[0] - 0.02 * eigenvectors[1, 0] * eigenvalues[1, 0], cntr[1] - 0.02 * eigenvectors[1, 1] * eigenvalues[1, 0])
    cv.circle(img, (int(p1[0]), int(p1[1])), 3, (0, 0, 255), 2)
    cv.circle(img, (int(p2[0]), int(p2[1])), 3, (255, 0, 0), 2)
    drawAxis(img, cntr, p1, (0, 0, 255), 1)
    drawAxis(img, cntr, p2, (255, 0, 0), 2)
    # orientation in radians
    angle = atan2(eigenvectors[0, 1], eigenvectors[0, 0])

    cv.putText(img, F'{angle:.3}', cntr, cv.FONT_HERSHEY_SIMPLEX, 0.8, (155, 136, 254), 2)
    m = cv.getRotationMatrix2D(cntr, angle * 180 / pi, 1)

    newp = np.ndarray((sz, 1, 2), dtype=np.int32)
    for i, p in enumerate(data_pts):
        px = p[0] * m[0, 0] + p[1] * m[0, 1] + m[0, 2]
        py = p[0] * m[1, 0] + p[1] * m[1, 1] + m[1, 2]
        newp[i, 0, 0] = int(px)
        newp[i, 0, 1] = int(py)

    rect = cv.boundingRect(newp)
    rrect = ((rect[0] + 0.5*rect[2], rect[1] + 0.5 * rect[3]), (rect[2], rect[3]), 0)
    points = cv.boxPoints(rrect)

    m = cv.getRotationMatrix2D(cntr, -angle * 180 / pi, 1)
    newp = list()
    for i, p in enumerate(points):
        px = p[0] * m[0, 0] + p[1] * m[0, 1] + m[0, 2]
        py = p[0] * m[1, 0] + p[1] * m[1, 1] + m[1, 2]
        newp.append((px, py))

    return newp, rect


src = cv.imread('20210123011911.png')
if src is None:
    exit(0)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
_, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
for i, c in enumerate(contours):
    area = cv.contourArea(c)
    if area < 1e2 or 1e5 < area:
        continue

    newp, rect = getOrientation(c, src)

    for i in range(len(newp)):
        ps = (int(newp[i][0]), int(newp[i][1]))
        pe = (int(newp[(i+1) % 4][0]), int(newp[(i+1) % 4][1]))
        cv.line(src, ps, pe, (0, 255, 0), 2)
        cv.putText(src, str(i), ps, cv.FONT_HERSHEY_SIMPLEX, 0.8, (155, 136, 254), 2)

    src_points = np.ndarray((4, 1, 2), dtype=np.float32)
    for i, p in enumerate(newp):
        src_points[i, 0, 0] = p[0]
        src_points[i, 0, 1] = p[1]

    dst_points = np.array([[0, rect[3]-1], [0, 0], [rect[2]-1, 0], [rect[2]-1, rect[3]-1]], dtype="float32")
    trans = cv.getPerspectiveTransform(src_points, dst_points, cv.DECOMP_LU)
    warped = cv.warpPerspective(src, trans, (rect[2], rect[3]))
    cv.imshow('dst', warped)
    cv.waitKey()

cv.imshow('output', src)
cv.waitKey()
cv.destroyAllWindows()
