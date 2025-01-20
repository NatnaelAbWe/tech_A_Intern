import cv2
import numpy as np

def load_image(image_path):
    """Loads an image from the specified path and returns the image object."""
    image = cv2.imread(image_path)
    if image is None:
        print("❌ Error: Unable to load image. Please check the file path.")
        exit()
    return image

def preprocess_image(image):
    """Converts the image to grayscale, applies Gaussian blur, and detects edges using Canny."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    return edged

def find_document_contour(edged, image):
    """Finds the largest contour that represents the document."""
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        if len(approx) == 4:  # Ensures the contour is a quadrilateral
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
            return image

    print("⚠️ No document-like contour detected.")
    return image

def main(image_path):
    """Main function to process and save the scanned document."""
    image = load_image(image_path)
    edged = preprocess_image(image)
    processed_image = find_document_contour(edged, image)

    output_path = "scanned_document.jpg"
    cv2.imwrite(output_path, processed_image)
    print(f"✅ Scanned document saved as '{output_path}'")

    # Display the result
    cv2.imshow("Scanned Document", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "level3.jpg"  # Change to the path of your image
    main(image_path)
