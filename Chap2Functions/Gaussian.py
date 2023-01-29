import cv2

img = cv2.imread('../Resources/cards.jpg')


imgBlur = cv2.GaussianBlur(img, (7, 7), 1)

cv2.imshow("output", imgBlur)

cv2.waitKey(0) and 0xFF == ord('q')

cv2.destroyAllWindows()
