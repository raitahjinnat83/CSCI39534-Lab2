# Task 1: Perform operations involving image addition and alpha blending on grayscale images.

# Image Addition: first image = plane, second image = car

# Ensure clipped resulting pixel values to remain within valid range of display

# import packagaes for images and arrays
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageChops

image_1 = Image.open("plane.png").convert("RGBA") # for alpha blending later
image_2 = Image.open("car.png").convert("RGBA")

image_2 = image_2.resize(image_1.size) # make sure images are same size

# applying addition method
# image_3 = ImageChops.add(image_1, image_2, scale=1.0,offset=0)

# image_3.show()

# image_3.save("plane_and_car.png")

# Alpha Blending: 

# Set alpha blending factors
a_less = 0.2
a_half = 0.5  
a_greater = 0.8

# Blend images
blended_image_less = Image.blend(image_1, image_2, a_less)
blended_image_half = Image.blend(image_1, image_2, a_half)
blended_image_greater = Image.blend(image_1, image_2, a_greater)

# Show and save the results
blended_image_less.show()
blended_image_less.save("blended_a_less.png")

blended_image_half.show()
blended_image_half.save("blended_a_half.png")

blended_image_greater.show()
blended_image_greater.save("blended_a_greater.png")