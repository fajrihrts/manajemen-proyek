def encrypt(plaintext, key):
    """
    Melakukan enkripsi plaintext menggunakan kunci key.
    """
    ciphertext = ""
    for char in plaintext:
        # Convert to numeric value
        char_num = ord(char)
        # Apply Caesar cipher transformation
        new_char_num = (char_num + key) % 256
        # Convert back to character
        new_char = chr(new_char_num)
        ciphertext += new_char
    return ciphertext


def decrypt(ciphertext, key):
    """
    Melakukan dekripsi ciphertext menggunakan kunci key.
    """
    plaintext = ""
    for char in ciphertext:
        # Convert to numeric value
        char_num = ord(char)
        # Apply inverse Caesar cipher transformation
        new_char_num = (char_num - key) % 256
        # Convert back to character
        new_char = chr(new_char_num)
        plaintext += new_char
    return plaintext


# Ask for user input for plaintext and key
plaintext = input("Masukkan plaintext: ")
key = int(input("Masukkan kunci enkripsi: "))

# Test the functions
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

# Print the results
print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted text: ", decrypted_text)

# Penjelasan singkat:

# Program ini meminta input dari pengguna untuk plaintext dan kunci enkripsi menggunakan fungsi input().
# Fungsi encrypt dan decrypt adalah sama dengan contoh sebelumnya.
# Setelah melakukan enkripsi dan dekripsi, program mencetak hasilnya menggunakan fungsi print().
