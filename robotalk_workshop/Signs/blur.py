import cv2

def blur_image(image_path, output_path, kernel_size=(25, 25)):
    # Load the image
    image = cv2.imread(image_path)
    
    # Blur the image
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    
    # Save the blurred image
    cv2.imwrite(output_path, blurred_image)

# Example usage
blur_image('stop.jpg', 'blurred_stop.jpg')
