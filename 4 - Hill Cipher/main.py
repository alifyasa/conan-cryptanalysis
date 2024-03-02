import numpy as np

def matrix_modulo_inverse(matrix, modulus):
    mat_det = np.round(np.linalg.det(matrix)).astype(int)
    return np.round(
        (
            np.linalg.inv(matrix) 
            * mat_det 
            * pow(int(mat_det), -1, modulus)
        ) % modulus
    ).astype(int)

def str_to_matrix(string):
    mat = np.array([ord(char) - ord('A') for char in string.upper()])

    if len(mat) % 3 != 0:
        raise ValueError("Length of array is not divisible by 3")
    
    return mat.reshape(-1, 3).T

def matrix_to_str(mat):
    string = ''
    for col in mat.T:
        string += ''.join([chr(int(val) + ord('A')) for val in col])
    return string

def load_ciphertext(ciphertext_file = "ciphertext.txt"):
        with open(ciphertext_file, "r") as f:
            return ''.join(f.read().split())

if __name__ == "__main__":

    modulus = 26
    ciphertext = load_ciphertext()
    ciphertext_mat = str_to_matrix(ciphertext)

    # Known Plaintext Attack to get Key
    known_plaintext_mat  = str_to_matrix("HELLOAIHA")
    known_ciphertext_mat = ciphertext_mat[:3, :3]

    print(f"{'Known Plaintext':<20}: {matrix_to_str(known_plaintext_mat)}")
    print(f"{'Known Ciphertext':<20}: {matrix_to_str(known_ciphertext_mat)}")

    key_mat = (known_ciphertext_mat @ matrix_modulo_inverse(known_plaintext_mat, modulus)) % modulus
    key = matrix_to_str(key_mat)

    print(f"{'Key':<20}: {key}")

    # Decrypt using Key
    plaintext_mat = (matrix_modulo_inverse(key_mat, modulus) @ ciphertext_mat) % 26
    plaintext = matrix_to_str(plaintext_mat)

    print("========== PLAINTEXT ==========")
    print(plaintext)