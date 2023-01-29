import cv2
import numpy as np

img = cv2.imread('Resources/danish.jpg')

imgResize = cv2.resize(img, (720, 600))

img2 = cv2.line(imgResize, (0, 0), (300, 265), (255, 0, 0), 2)
img2 = cv2.line(imgResize, (725, 0), (300, 265), (255, 0, 0), 2)
img2 = cv2.line(imgResize, (0, 600), (300, 265), (255, 0, 0), 2)
img2 = cv2.line(imgResize, (725, 600), (300, 265), (255, 0, 0), 2)
img2 = cv2.rectangle(imgResize, (0, 0), (720, 600), (1233, 0, 0), 5)
img2 = cv2.putText(imgResize, "Danish", (300, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 4)
cv2.imshow('img', img2)

cv2.waitKey(0)
