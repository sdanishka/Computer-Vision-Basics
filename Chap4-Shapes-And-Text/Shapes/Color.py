import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255, 0, 0

cv2.imshow("output", img)

cv2.waitKey(30000) and 0xFF == ord('q')


cv2.destroyAllWindows()
