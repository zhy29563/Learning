import cv2 as cv
import numpy as np


def math_demo(m1, m2):
    cv.imshow("add_demo", cv.add(m1, m2))
    cv.imshow("sub_demo", cv.subtract(m1, m2))
    cv.imshow("mul_demo", cv.multiply(m1, m2))
    cv.imshow("div_demo", cv.divide(m1, m2))


def logic_demo(m1, m2):
    cv.imshow("and_demo", cv.bitwise_and(m1, m2))
    cv.imshow("or_demo", cv.bitwise_or(m1, m2))
    cv.imshow("not_demo", cv.bitwise_not(m1, m2))


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1 - c, b)
    cv.imshow("con-bri-demo", dst)


def others(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


print("--------- Hello Python ---------")
src1 = cv.imread("../images/LinuxLogo.jpg")
src2 = cv.imread("../images/WindowsLogo.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)

# src = cv.imread("../images/lena.png")
# cv.imshow("image2", src)
# contrast_brightness_demo(src, 1.5, 0)

math_demo(src1, src2)
logic_demo(src1, src2)
# others(src1, src2)


cv.waitKey(0)
cv.destroyAllWindows()
