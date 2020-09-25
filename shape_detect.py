import cv2 as cv
import numpy as np
import random

from img_stacker import stack_images


def get_contours(img, img_contour):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for con in contours:
        area = cv.contourArea(con)
        if area > 3000:
            cv.drawContours(img_contour, con, -1, (255, 0, 0), 3)
            perimeter = cv.arcLength(con, True)
            corners = cv.approxPolyDP(con, 0.005*perimeter, True)
            print(len(corners))
            object_corners = len(corners)
            x, y, width, height = cv.boundingRect(corners)
            object_type = None
            if object_corners == 3:
                object_type = "Triangle"
            elif object_corners == 4:
                asp_ratio = width / float(height)
                if asp_ratio > 0.95 and asp_ratio < 1.05:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif object_corners == 5:
                object_type = "Pentagon"
            elif object_corners == 5:
                object_type = "Hexagon"
            elif object_corners > 10:
                asp_ratio = width / float(height)
                if asp_ratio > 0.9 and asp_ratio < 1.1:
                    object_type = "Circle"
                else:
                    object_type = "Blob"
            if object_type is not None:
                if object_type == "Blob":
                    ran_num = random.randrange(0, 10)
                    if ran_num == 0:
                        pass
                    else:
                        break
                cv.putText(img_contour, object_type, (int(x + width / 2 - 10), int(y + height / 2 - 10)), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
                cv.rectangle(img_contour, (x, y), (x + width, y + height), (0, 255, 0), 3)


if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    path = 'Resources/shapes.png'
    while True:
        success, img = cap.read()
        img_contour = img.copy()
        img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_blur = cv.GaussianBlur(img_grey, (7, 7), 2)
        imgCanny = cv.Canny(img_blur, 50, 50)
        get_contours(imgCanny, img_contour)
        img_stack = stack_images(.8, [imgCanny, img_contour])
        cv.imshow("Shapes", img_stack)
        cv.waitKey(1)
