from skimage import io, util
import matplotlib.pyplot as plt

def add_gaussian_noise(image_path, output_path, mode='gaussian', amount=0.01):
    # Load the image
    image = io.imread(image_path)
    
    # Add noise
    noisy_image = util.random_noise(image, mode=mode, var=amount)
    
    # Convert the image pixel values to the correct type
    noisy_image = (255 * noisy_image).astype("uint8")
    
    # Save the noisy image
    io.imsave(output_path, noisy_image)

    # Optionally, display the noisy image
    plt.imshow(noisy_image)
    plt.show()

# Example usage
add_gaussian_noise('stop.jpg', 'noisy_stop.jpg')
