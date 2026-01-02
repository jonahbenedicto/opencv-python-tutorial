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
image = cv2.imread('image.jpg)
```

# Extracting the Height and Width of an Image

```python
height, width = image.shape[:2]
```

# Extracting the RGB Values of a Pixel 
This is the code to be able extract an RGB value of a pixel at the point (100, 100):
```python
(B, G, R) = image[100, 100]
```

This is the code to be able to extract the value of a specific channel at the point (100, 100):
```python
B = image[100, 100, 0]
```

# Extract the Region of Interest (ROI)
```python

```
