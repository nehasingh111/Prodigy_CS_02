"""Develop a simple image encryption tool using pixel manipulation. 
You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. 
Allow users to encrypt and decrypt images."""

from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB format
    img_array = np.array(img)

    # Encrypt the image by adding the key to each pixel
    encrypted_array = (img_array.astype(np.uint16) + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'), 'RGB')

    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(encrypted_path, output_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    img = img.convert("RGB")
    img_array = np.array(img)

    # Decrypt the image by subtracting the key from each pixel
    decrypted_array = (img_array.astype(np.uint16) - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'), 'RGB')

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    original_image_path = "test.png"
    encrypted_image_path = "encrypted_img.png"
    decrypted_image_path = "decrypted_img.png"
    encryption_key = 50  # Example key for encryption and decryption

    encrypt_image(original_image_path, encrypted_image_path, encryption_key)
    decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)