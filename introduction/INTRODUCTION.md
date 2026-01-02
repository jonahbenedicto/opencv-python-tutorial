# Introduction

# Table of Contents
- [Code](#code)
- [Import OpenCV Library](#import-opencv-library)
- [Reading An Image](#reading-an-image)
- [Extracting the Height and Width of an Image](#extracting-the-height-and-width-of-an-image)
- [Extracting the RGB Values of a Pixel](#extracting-the-rgb-values-of-a-pixel) 


# Code
- [Reading an Image](./read-image.py)
- [Extracting the RGB values of a pixel](./extract-rgb.py)
- [Extracting the Region of Interest (ROI)]()
- [Resizing the Image]()
- [Rotating the Image]()
- [Drawing a Rectangle]()
- [Displaying a Text]()

# Import OpenCV Library
```python
import cv2
```

# Reading an Image

```python
import cv2

image = cv2.imread('image.jpg)
```

# Extracting the Height and Width of an Image

```python
import cv2
image = cv2.imread("image.png")

height, width = image.shape[:2]
```

# Extracting the RGB Values of a Pixel 
```python
import cv2
image = cv2.imread("image.png")

(B, G, R) = image[100, 100]
```

Extracting colour value from specific colour channel
```python
import cv2
image = cv2.imread("image.png")

B = image[100, 100, 0]
```

# Extracting the Region of Interest (ROI)
```python
import cv2
image = cv2.imread("image.png")

roi = image[500 : 800, 200 : 600]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
```

# Resizing the Image

```python
import cv2
image = cv2.imread("image.png")

resize = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)
```

Maintain a proper aspect ratio
```python
import cv2

image = cv2.imread("image.png")

height, width = image.shape[:2]

ratio = 800 / width

dimension = (800, int(height * ratio))

resize_aspect = cv2.resize(image, dimension)
cv2.imshow("Resized Image", resize_aspect)
cv2.waitKey(0)
```

# Drawing a Rectangle

```python
import cv2
image = cv2.imread("image.png")

output = image.copy()
rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (255, 0, 0), 2)
```

# Displaying Text

```python
import cv2
image = cv2.imread("image.png")

output = image.copy()

text = cv2.putText(output, 'OpenCV Demo', (500, 550), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
```
