import cv2

# Read image
image = cv2.imread('image.png')

# Extract RGB at random point
(B, G, R) = image[100, 100]
print("R = {}, G = {}, B = {}".format(R, G, B))

# Extract B at random point
B = image[100, 100, 0]
print("B = {}".format(B))
