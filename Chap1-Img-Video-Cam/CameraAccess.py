import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 620)
cap.set(10, 10)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow('output', img)
    if cv2.waitKey(30) and 0xFF == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()
