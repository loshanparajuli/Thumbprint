import cv2

def save_processed_image(image, output_path):
    cv2.imwrite(output_path, image)