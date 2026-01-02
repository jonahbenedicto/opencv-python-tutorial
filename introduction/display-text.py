import cv2
image = cv2.imread("image.png")

output = image.copy()

text = cv2.putText(output, 'OpenCV Demo', (500, 550), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
