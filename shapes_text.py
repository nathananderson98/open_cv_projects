import cv2 as cv
import numpy as np

if __name__ == '__main__':
    img = np.zeros((512, 512, 3), np.uint8)
    img[:] = 255,0,0
    cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0,0,255), 4)
    cv.rectangle(img, (0,0), (250, 350), (0,255,0), cv.FILLED)
    cv.circle(img, (400, 50), 30, (255, 255, 30), 5)
    cv.putText(img, "Working", (30, 400), cv.FONT_HERSHEY_PLAIN, 5, (0,0,0), 3)
    cv.imshow("Image", img)
    cv.waitKey(0)
