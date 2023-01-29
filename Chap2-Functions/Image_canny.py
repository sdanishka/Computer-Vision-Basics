import cv2

img = cv2.imread('../Resources/cards.jpg')


imgCanny = cv2.Canny(img, 150, 220)

cv2.imshow("output", imgCanny)

cv2.waitKey(30000) and 0xFF == ord('q')

cap.release()
cv2.destroyAllWindows()
