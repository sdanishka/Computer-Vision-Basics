import cv2

img = cv2.imread('../Resources/danish.jpg')

imgResize = cv2.resize(img, (620, 600))

print("Img Resize: ", imgResize.shape)
cv2.imshow("output1", imgResize)         # Resize image

imgCropped = img[0:400, 100:500]

cv2.imshow("output2", imgCropped)         # Cropped image

cv2.waitKey(30000) and 0xFF == ord('q')

cap.release()
cv2.destroyAllWindows()
