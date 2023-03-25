import cv2

def load_image(file_path):
    img = cv2.imread(file_path)
    return img
