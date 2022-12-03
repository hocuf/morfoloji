import cv2
import numpy as np


    kernel = np.ones((45,45),np.uint8)

    cap = cv2.VideoCapture(0)

    while True:
        img, process = cap.read()
        dilation = cv2.morphologyEx(process,cv2.MORPH_DILATE,kernel)
        erosion = cv2.morphologyEx(process,cv2.MORPH_ERODE,kernel)
        opening = cv2.morphologyEx(process,cv2.MORPH_OPEN,kernel)
        cv2.imshow("DILATION",dilation)
        cv2.imshow("EROSION",erosion)
        cv2.imshow("OPENING",opening)

        cv2.waitKey(1)