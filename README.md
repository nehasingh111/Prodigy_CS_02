Image Encryption Tool:
This simple image encryption tool uses pixel manipulation to encrypt and decrypt images. It adds a specified key value to each pixel's RGB values for encryption and subtracts the same key for decryption.

Prerequisites:
Python 3.x
Pillow library (PIL)
numpy library
You can install the required libraries using pip:

Bash:
pip install Pillow numpy

Usage:
Encryption: To encrypt an image, call the encrypt_image function
Decryption: To decrypt an image, call the decrypt_image function

How It Works
The tool converts the image to an RGB format and then to a NumPy array for easy pixel manipulation.
During encryption, the tool adds the key to each pixel's RGB values and wraps around using modulo 256 to keep the values within valid range (0-255).
During decryption, it subtracts the key from each pixel's RGB values, again using modulo 256 for wrapping around.

Example
Original Image: test.png
Encrypted Image: encrypted_img.png (created by adding 50 to each pixel's RGB values)
Decrypted Image: decrypted_img.png (retrieved by subtracting 50 from each pixel's RGB values)

Important Note
This is a simple encryption method and should not be used for securing sensitive information. It is intended for educational purposes and basic image manipulation.

License
This project is open-source and available under the MIT License.