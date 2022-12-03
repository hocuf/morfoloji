import cv2
import  numpy as np

kernel = np.ones((15,5), np.uint8)
image = cv2.imread("image.jpeg",0)
wanted = cv2.resize(image,(400,400))

erosion = cv2.erode(wanted,kernel)
dilation = cv2.dilate(wanted,kernel,iterations=2)
opening = cv2.morphologyEx(wanted,cv2.MORPH_OPEN,kernel)
closing= cv2.morphologyEx(wanted,cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(wanted, cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(wanted, cv2. MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(wanted, cv2.MORPH_BLACKHAT,kernel)

unknown = cv2.subtract(dilation,kernel)



"""

https://homepages.inf.ed.ac.uk/rbf/HIPR2/morops.htm  - this webb page is except morphology

"""
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)
cv2.imshow("pother", unknown)
cv2.waitKey(0)
