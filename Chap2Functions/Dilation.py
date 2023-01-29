import cv2
import numpy as np

img = cv2.imread('../Resources/cards.jpg')
kernal = np.ones((5, 5), np.uint8)


imgCanny = cv2.Canny(img, 150, 220)
imgDilation = cv2.dilate(imgCanny, kernal, iterations=1)

cv2.imshow("output", imgDilation)

cv2.waitKey(30000) and 0xFF == ord('q')

cap.release()
cv2.destroyAllWindows()
