import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

imgRaw = np.zeros((2000,2000),dtype=np.uint8)

time1 = cv.getCPUTickCount()
circle1 = cv.rectangle(imgRaw, (1251, 50), (1216, 1307), (255, 255, 255), -1)
time2 = cv.getCPUTickCount()
print((time2 - time1) / cv.getTickFrequency())
