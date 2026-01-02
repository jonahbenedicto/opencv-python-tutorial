import cv2

# Read image
image = cv2.imread('image.png')

# Extract height and width
height, width = image.shape[:2]
print("Height = {}, Width = {}".format(height, width))
