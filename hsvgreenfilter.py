'''
Created: September 28, 2018
Modified: Sepetember 29, 2018

Program to detect the colors of traffic signals using HSV values.

Value of HSV thresholds for the China-based traffic sign color:
Red: 
    H>=240 or H<=10
    S>= 40
    V>= 30
Yellow:
    18<=H<=45 
    S>=148
    V>=66
Green: [60, 255, 255]
'''

import cv2 as cv
from cv2 import dnn
import numpy as np

img = cv.imread('sample.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

'''
#define range of yellow color in HSV
lower_yellow = np.array([18, 148, 66])
upper_yellow = np.array([45, 255, 255])

#threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

#bitwise-AND mask and original image
res = cv.bitwise_and(img, img, mask = mask)

cv.imshow('yellow lights (original)',hsv)
cv.imshow('yellow lights (HSV)', mask)
cv.imshow('yellow lights (masked)', res)
'''

#define range of green color in HSV
lower_green = np.array([50, 50, 120])
upper_green = np.array([70, 255, 255])

#threshold the HSV image to get only green colors
mask = cv.inRange(hsv, lower_green, upper_green)

#bitwise-AND mask and original image
res = cv.bitwise_and(img, img, mask = mask)

cv.imshow('green lights (masked)', hsv)

cv.waitKey(0)
cv.destroyAllWindows()
