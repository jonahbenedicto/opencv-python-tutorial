import cv2

# Read Image
image = cv2.imread("image.png")

# Resize Image
resize = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)

# Extract Dimensions
height, width = image.shape[:2]

# Calculate the ratio
ratio = 800 / width

# Creating a tuple containing width and height
dimension = (800, int(height * ratio))

# Resize Image
resize_aspect = cv2.resize(image, dimension)
cv2.imshow("Resized Image", resize_aspect)
cv2.waitKey(0)
