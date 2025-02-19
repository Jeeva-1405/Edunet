import cv2
import os

def create_mappings():
    return {chr(i): i for i in range(256)}

def encrypt_message(img, msg):
    d = create_mappings()
    rows, cols, _ = img.shape
    total_pixels = rows * cols * 3
    
    if len(msg) > total_pixels:
        raise ValueError("Message too long to encode in this image.")
    
    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == cols:
                m = 0
                n += 1
    
    return img

def main():
    image_path = "white.png"
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    encrypted_img = encrypt_message(img, msg)
    cv2.imwrite("encryptedImage.png", encrypted_img)
    os.system("start encryptedImage.png")
    
    with open("key.txt", "w") as f:
        f.write(password + "\n" + str(len(msg)))
    
    print("Encryption complete! Image saved as encryptedImage.png")

if __name__ == "__main__":
    main()
