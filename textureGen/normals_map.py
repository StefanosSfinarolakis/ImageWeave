import cv2
import numpy as np
from load_image import load_image

def calculate_normal_map(file_path):
    # Load the input image
    img = load_image(file_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate the gradient in the x and y directions
    dx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    dy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)

    # Normalize the gradient values to the range [-1, 1]
    dx = cv2.normalize(dx, None, -1, 1, cv2.NORM_MINMAX)
    dy = cv2.normalize(dy, None, -1, 1, cv2.NORM_MINMAX)
    
    # Calculate the normal map
    normal_map = np.dstack((dx, dy, np.zeros_like(dx)))

    # Normalize the normal map values to the range [0, 255]
    normal_map = cv2.normalize(normal_map, None, 0, 255, cv2.NORM_MINMAX)
    
    return normal_map