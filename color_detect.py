import cv2 as cv
import numpy as np

def empty(a):
    pass


if __name__ == '__main__':
    cap = cv.VideoCapture(0)

    cv.namedWindow("track_bars")
    cv.resizeWindow("track_bars", 640, 240)
    cv.createTrackbar("Hue Min", "track_bars", 97, 179, empty)
    cv.createTrackbar("Hue Max", "track_bars", 131, 179, empty)
    cv.createTrackbar("Sat Min", "track_bars", 158, 255, empty)
    cv.createTrackbar("Sat Max", "track_bars", 255, 255, empty)
    cv.createTrackbar("Val Min", "track_bars", 103, 255, empty)
    cv.createTrackbar("Val Max", "track_bars", 255, 255, empty)

    while True:
        success, img = cap.read()
        imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        h_min = cv.getTrackbarPos("Hue Min", "track_bars")
        h_max = cv.getTrackbarPos("Hue Max", "track_bars")
        s_min = cv.getTrackbarPos("Sat Min", "track_bars")
        s_max = cv.getTrackbarPos("Sat Max", "track_bars")
        v_min = cv.getTrackbarPos("Val Min", "track_bars")
        v_max = cv.getTrackbarPos("Val Max", "track_bars")
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv.inRange(imgHSV, lower, upper)
        img_result = cv.bitwise_and(img, img, mask=mask)  # makes the masked video with the bitwise function
        img_hor = np.hstack((img, img_result))
        # cv.imshow("RGB", img)
        # cv.imshow("HSV", imgHSV)
        cv.imshow("Result", img_hor)
        cv.waitKey(1)

