import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 0, 0, 0

img2 = cv2.circle(img, (300, 50), 30, (255, 0, 0), 2)

cv2.imshow("output", img2)

cv2.waitKey(30000) and 0xFF == ord('q')

cv2.destroyAllWindows()
