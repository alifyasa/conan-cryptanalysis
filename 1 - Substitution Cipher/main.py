def get_substitution_dict(key: str):
    subs_dict = {}
    for i in range(26):
        subs_dict[chr(i + ord('A'))] = key[i]
    return subs_dict


def substitution_decrypt(ciphertext: str, key: str):
    subs_dict = get_substitution_dict(key)
    result = ''
    for ciphertext_char in ciphertext:
        if ciphertext_char.isalpha():
            result += subs_dict[ciphertext_char]
        else:
            result += ciphertext_char
    return result

def load_ciphertext(ciphertext_path: str = "ciphertext.txt"):
    with open(ciphertext_path, "r") as f:
        return ''.join(f.read().split())

def main():
    ciphertext = load_ciphertext()
    key = "SRDXENFTKJBIYVGMQOZWUPLCAH"
    plaintext = substitution_decrypt(ciphertext, key)

    print(f"Key: {key}")
    print("========== PLAINTEXT ==========")
    print(plaintext)

if __name__ == "__main__":
    main()