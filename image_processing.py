import cv2
from matplotlib import pyplot as plt

def enhance_image(gray_image):
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    equalized_image = cv2.equalizeHist(blurred_image)
    
    plt.figure(figsize=(5, 5))
    plt.title('Enhanced Image')
    plt.imshow(equalized_image, cmap='gray')
    plt.show()
    
    return equalized_image

def extract_fingerprint_features(enhanced_image):
    _, binary_image = cv2.threshold(enhanced_image, 127, 255, cv2.THRESH_BINARY_INV)
    edges = cv2.Canny(binary_image, 100, 200)
    
    plt.figure(figsize=(5, 5))
    plt.title('Edges of Fingerprint')
    plt.imshow(edges, cmap='gray')
    plt.show()
    
    return edges