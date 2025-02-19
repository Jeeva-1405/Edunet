import cv2

def create_mappings():
    return {i: chr(i) for i in range(256)}

def decrypt_message(img, length):
    c = create_mappings()
    rows, cols, _ = img.shape
    message = ""
    n, m, z = 0, 0, 0
    
    for _ in range(length):
        message += c[img[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == cols:
                m = 0
                n += 1
    
    return message

def main():
    image_path = "encryptedImage.png"
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    try:
        with open("key.txt", "r") as f:
            saved_password, length = f.read().split("\n")
            length = int(length)
    except:
        print("Error: Key file not found or corrupted!")
        return
    
    pas = input("Enter passcode for decryption: ")
    if pas == saved_password:
        decrypted_msg = decrypt_message(img, length)
        print("Decrypted message:", decrypted_msg)
    else:
        print("YOU ARE NOT AUTHORIZED")

if __name__ == "__main__":
    main()
