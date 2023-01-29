import cv2

img = cv2.imread('../Resources/cards.jpg')

cv2.imshow("output", img)
cv2.waitKey(30000) and 0xFF == ord('q')

cap.release()
cv2.destroyAllWindows()
