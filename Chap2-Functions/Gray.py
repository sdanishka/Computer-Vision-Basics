import cv2

img = cv2.imread('../Resources/cards.jpg')


imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("output", imgGrey)

cv2.waitKey(30000) and 0xFF == ord('q')

img.release()
cv2.destroyAllWindows()