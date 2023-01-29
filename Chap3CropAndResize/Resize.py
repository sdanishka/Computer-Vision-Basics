import cv2

img = cv2.imread('../Resources/danish.jpg')

print("Img Resize: ", img.shape)
cv2.imshow("output1", img)               # Original Image

imgResize = cv2.resize(img, (620, 600))

print("Img Resize: ", imgResize.shape)
cv2.imshow("output2", imgResize)         # Resize image


cv2.waitKey(30000) and 0xFF == ord('q')

cap.release()
cv2.destroyAllWindows()
