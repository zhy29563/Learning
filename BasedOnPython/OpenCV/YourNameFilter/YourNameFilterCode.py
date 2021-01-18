import cv2 as cv

if __name__ == '__main__':
    src = cv.imread('src.jpg')
    cv.imshow("src", src)
    cloud = cv.imread('cloud.jpg')

    # 1. 背景（天空）分割
    src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    src_h, src_s, src_v = cv.split(src_hsv)
    src_v = cv.equalizeHist(src_v)

    cv.waitKey()
