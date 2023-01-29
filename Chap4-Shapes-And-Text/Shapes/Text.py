import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255, 0, 0

img2 = cv2.putText(img, "Danish Khan Afridi", (100, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (2, 200, 1), 1)

cv2.imshow("output", img2)

cv2.waitKey(30000) and 0xFF == ord('q')

cv2.destroyAllWindows()
