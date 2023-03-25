import cv2
import numpy as np
from load_image import load_image

def calculate_height_map(file_path):
    # Load the input image
    img = load_image(file_path, 0)

    # Normalize the gradient values to the range [0, 1]
    img = cv2.normalize(img, None, 0, 1, cv2.NORM_MINMAX)

    # Invert the image
    img = 1.0 - img

    # Calculate the height map by scaling the image values
    height_map = img * 255

    # Convert the height map to a 8-bit unsigned integer
    height_map = height_map.astype(np.uint8)
    
    return height_map
