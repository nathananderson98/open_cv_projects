import cv2 as cv
import numpy as np

if __name__ == '__main__':
    img = cv.imread('Resources/Temple_Slant.png')
    img_hor = np.hstack((img, img))
    img_ver = np.vstack((img, img))
    cv.imshow("Stacked Horizontal", img_hor)
    cv.imshow("Stacked Vertical", img_ver)
    cv.waitKey(2000)
