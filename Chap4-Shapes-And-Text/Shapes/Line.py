import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (255, 0, 0), 3)      # Full line
cv2.line(img, (0, 0), (300, 400), (0, 0, 255), 3)                        # Half line

cv2.imshow("output", img)

cv2.waitKey(30000) and 0xFF == ord('q')


cv2.destroyAllWindows()
