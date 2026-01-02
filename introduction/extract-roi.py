import cv2

image = cv2.imread("image.png")

roi = image[500 : 800, 200 : 600]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
