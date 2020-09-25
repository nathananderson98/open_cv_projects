import cv2 as cv
import numpy as np

if __name__ == '__main__':
    img = cv.imread("Resources/Temple_Slant.png")
    width,height = 850, 1150
    pts1 = np.float32([[478, 186], [878, 197], [379, 516], [1078, 524]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    img_output = cv.warpPerspective(img, matrix, (width, height))
    cv.imshow("Temple", img)
    cv.imshow("Temple_warp", img_output)
    cv.waitKey(0)
