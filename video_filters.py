import cv2
import numpy as np

# Press the green button in the gutter to run the script
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)


    while True:
        success, img = cap.read()
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_grey, (7,7), 0)
        #  img_resize = cv2.resize(img, (1280, 1280))
        img_cropped = img[200:520, 200:1000]
        # cv2.imshow("Webcam_grey", img_grey)
        # cv2.imshow("Webcam_blur", img_blur)
        cv2.imshow("Webcam", img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break


