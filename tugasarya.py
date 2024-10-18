import os

def encrypt_text(text):
    # Shift each character by 3 in the ASCII table
    encrypted_text = ''.join(chr(ord(char) + 3) for char in text)
    return encrypted_text

def decrypt_text(text):
    # Shift each character by -3 in the ASCII table to reverse the encryption
    decrypted_text = ''.join(chr(ord(char) - 3) for char in text)
    return decrypted_text

def create_and_open_file(mode, filename):
    # Define the path for the Downloads directory
    downloads_path = r"C:\Users\ASUS\Downloads"

    # File path based on the user-provided filename
    file_path = os.path.join(downloads_path, f"{filename}.txt")
    
    try:
        if mode == "encrypt":
            # Get user input for the text to be encrypted
            original_text = input("Enter the text you want to encrypt: ")
            encrypted_text = encrypt_text(original_text)
            
            # Encrypt the text and write it to the file
            with open(file_path, "w") as file:
                file.write(encrypted_text)
            print(f"File encrypted and created at: {file_path}")
            os.startfile(file_path)  # Open the file

        elif mode == "decrypt":
            # Read the encrypted file and decrypt the content
            with open(file_path, "r") as file:
                encrypted_text = file.read()
            decrypted_text = decrypt_text(encrypted_text)
            
            # Write the decrypted text back to the file
            with open(file_path, "w") as file:
                file.write(decrypted_text)
            print(f"File decrypted and saved at: {file_path}")
            os.startfile(file_path)  # Open the file
            
    except FileNotFoundError:
        print("File not found. Please make sure the file exists when trying to decrypt.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    choice = input("Do you want to encrypt or decrypt the file? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    if choice in ["encrypt", "decrypt"]:
        filename = input("Enter the name of the file (without extension): ").strip()
        create_and_open_file(choice, filename)
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

main()