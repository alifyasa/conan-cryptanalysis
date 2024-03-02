def affine_decrypt(hex_values, m, b, n):
    cipher_hex = []
    for i in range(len(hex_values)):
        C = hex((pow(m, -1, n) * (int(hex_values[i], 16) - b)) % n)
        cipher_hex.append(C)
    return cipher_hex

def read_image_to_hex(image_path):
    try:
        with open(image_path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            array_of_hex = [hex(byte) for byte in b]
            return array_of_hex
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except ValueError as e:
        print("Error:", e)
    return None

def array_of_hex_to_bytearray(array_of_hex):
    bytearray_data = bytearray()
    for hex_value in array_of_hex:
        if hex_value.startswith('0x'):
            hex_value = hex_value[2:]
        byte_value = int(hex_value, 16)
        bytearray_data.append(byte_value)
    return bytearray_data

def create_file_from_bytes(file_path, bytes_data):
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_data)
        print("File berhasil dibuat:", file_path)
    except Exception as e:
        print("Error:", e)

def main():
    # Config
    modulus = 256
    image_path = "chall.jpg"
    hex_values = read_image_to_hex(image_path)

    # Get first two bytes
    fst_c_byte, snd_c_byte = hex_values[:2]
    fst_c_byte, snd_c_byte = int(fst_c_byte, 16), int(snd_c_byte, 16)

    # Known Plaintext from Magic Bytes
    fst_p_byte, snd_p_byte = int('0xFF', 16), int('0xD8', 16)

    # Assume formula of m * p + b % 256 = c
    # then (m * p1 + b) - (m * p2 + b) % 256 = c1 - c2
    # then m * (p1 - p2) % 256 = c1 - c2
    # then m = (c1 - c2) * pow(p1 - p2, -1, 256)
    m = (fst_c_byte - snd_c_byte) * pow(fst_p_byte - snd_p_byte, -1, modulus) % modulus

    # Assume formula of m * p + b % 256 = c, m known
    # b = c - m * p % 256
    b = (fst_c_byte - m * fst_p_byte) % modulus

    # Report
    print("================= REPORT =================")
    print("Encryption Function is m * P + b % 256 = C")
    print("P is the plaintext")
    print("C is the ciphertext")
    print(f"m is {m}")
    print(f"b is {b}")
    print("==========================================")


    # Decrypt Image
    if hex_values is not None:
        cipher_hex = affine_decrypt(hex_values, m, b, modulus)
        bytearray_cipher = array_of_hex_to_bytearray(cipher_hex)
        create_file_from_bytes("./flag/flag.jpg", bytearray_cipher)

if __name__ == "__main__":
    main()