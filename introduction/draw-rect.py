import cv2
image = cv2.imread("image.png")

output = image.copy()
rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (255, 0, 0), 2)
