import cv2
import numpy as np
from load_image import load_image

def ambient_occlusion(img, ksize, sigma_color, sigma_space):
    """
    Calculate the ambient occlusion map from an image using a bilateral filter.
    """
    blurred = cv2.bilateralFilter(img, ksize, sigma_color, sigma_space)
    occlusion = img - blurred
    occlusion = cv2.normalize(occlusion, None, 0, 1, cv2.NORM_MINMAX)
    return occlusion

# Load the input image using load_image function
img = load_image("input.jpg")

# Convert the image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Normalize the image values to the range [0, 1]
img = cv2.normalize(img, None, 0, 1, cv2.NORM_MINMAX)

# Calculate the ambient occlusion map
occlusion = ambient_occlusion(img, 21, 75, 75)

# Normalize the ambient occlusion map values to the range [0, 255]
occlusion = cv2.normalize(occlusion, None, 0, 255, cv2.NORM_MINMAX)

# Convert the ambient occlusion map to a 8-bit unsigned integer
occlusion = occlusion.astype(np.uint8)

# Save the ambient occlusion map as an image
cv2.imwrite("ambient_occlusion_map.png", occlusion)


