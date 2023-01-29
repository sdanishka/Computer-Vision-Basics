import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img1 = np.zeros((512, 512, 3), np.uint8)


cv2.rectangle(img, (0, 0), (300, 350), (1233, 0, 0), 5)                  # Not Filled
cv2.rectangle(img1, (0, 0), (250, 350), (0.0, 255), cv2.FILLED)          # Filled

cv2.imshow("output", img)
cv2.imshow("output1", img1)

cv2.waitKey(30000) and 0xFF == ord('q')

cv2.destroyAllWindows()
