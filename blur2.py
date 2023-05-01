import cv2

import numpy as np

img=cv2.imread("C:/Users/AMMU/Downloads/WhatsApp Image 2023-04-30 at 21.55.07.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,3)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,5)
color=cv2.bilateralFilter(img,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)
cv2.imshow("show",cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()