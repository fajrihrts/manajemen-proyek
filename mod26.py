def mod_inverse(a, m):
    """
    Mencari nilai invers modulus a terhadap m.
    """
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return 1

def encrypt(plaintext, a, b):
    """
    Melakukan enkripsi plaintext menggunakan kunci a dan b.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Convert to uppercase to simplify arithmetic
            char = char.upper()
            # Convert to number between 0 and 25
            char_num = ord(char) - ord('A')
            # Apply affine transformation
            new_char_num = (a * char_num + b) % 26
            # Convert back to letter
            new_char = chr(new_char_num + ord('A'))
            ciphertext += new_char
        else:
            # Non-alphabetic characters are left as-is
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, a, b):
    """
    Melakukan dekripsi ciphertext menggunakan kunci a dan b.
    """
    plaintext = ""
    # Find modular inverse of a
    a_inverse = mod_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            # Convert to uppercase to simplify arithmetic
            char = char.upper()
            # Convert to number between 0 and 25
            char_num = ord(char) - ord('A')
            # Apply inverse affine transformation
            new_char_num = (a_inverse * (char_num - b)) % 26
            # Convert back to letter
            new_char = chr(new_char_num + ord('A'))
            plaintext += new_char
        else:
            # Non-alphabetic characters are left as-is
            plaintext += char
    return plaintext

# Test the functions
plaintext = str(input("Masukkan teks yang akan dienkripsi: "))
a = 5
b = 8
ciphertext = encrypt(plaintext, a, b)
decrypted_text = decrypt(ciphertext, a, b)
print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted text: ", decrypted_text)

# Penjelasan singkat:

# Program ini meminta input dari pengguna untuk plaintext dan kunci enkripsi menggunakan fungsi input().
# Fungsi encrypt dan decrypt akan mengecek apakah karakter yang dienkripsi atau didekripsi adalah huruf, jika ya maka karakter tersebut akan dikonversi menjadi angka dan dilakukan enkripsi atau dekripsi menggunakan rumus Caesar Cipher dengan mod 26. Jika tidak, karakter tersebut langsung diabaikan.
# Karena kita menggunakan alfabet Inggris yang terdiri dari 26 huruf, maka kita menggunakan modulus 26 dalam kalkulasi enkripsi dan dekripsi.
# Setelah melakukan enkripsi dan dekripsi, program mencetak hasilnya menggunakan fungsi print().
