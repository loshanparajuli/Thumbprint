from image_loading import load_and_display_image
from image_processing import enhance_image, extract_fingerprint_features
from utils import save_processed_image

def main():
    image_path = 'thumb_photo.jpg'
    output_path = 'processed_fingerprint.jpg'
    
    gray_image = load_and_display_image(image_path)
    enhanced_image = enhance_image(gray_image)
    fingerprint_edges = extract_fingerprint_features(enhanced_image)
    save_processed_image(fingerprint_edges, output_path)

if __name__ == "__main__":
    main()