import cv2
import numpy as np
from load_image import load_image

def calculate_bump_map(file_path):
    # Load the input image
    img = load_image(file_path, 0)
    img = cv2.normalize(img, None, 0, 1, cv2.NORM_MINMAX)

    # Invert the image
    img = 1.0 - img

    # Calculate the gradient in the x and y directions
    dx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    dy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

    # Normalize the gradient values to the range [-1, 1]
    dx = cv2.normalize(dx, None, -1, 1, cv2.NORM_MINMAX)
    dy = cv2.normalize(dy, None, -1, 1, cv2.NORM_MINMAX)
    
    # Calculate the bump map
    bump_map = np.dstack((dx, dy, np.zeros_like(dx)))

    # Normalize the bump map values to the range [0, 255]
    bump_map = cv2.normalize(bump_map, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the bump map to a 8-bit unsigned integer
    bump_map = bump_map.astype(np.uint8)
    
    return bump_map
