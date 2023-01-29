import cv2

cap = cv2.VideoCapture('../Resources/Sample.mp4')

while True:
    success, img1= cap.read()
    cv2.imshow("output", img)
    if cv2.waitKey(30) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
