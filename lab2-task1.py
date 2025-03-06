# Task 1: Perform operations involving image addition and alpha blending on grayscale images.

# Image Addition: first image = plane, second image = car

# Ensure clipped resulting pixel values to remain within valid range of display

# import packagaes for images and arrays
import matplotlib.pyplot as plt
import numpy as numpy
from PIL import Image, ImageChops

image_1 = Image.open("plane.png")
image_2 = Image.open("car.png")

# applying addition method
image_3 = ImageChops.add(image_1, image_2)

image_3.show()

image_3.save("plane_and_car.png")