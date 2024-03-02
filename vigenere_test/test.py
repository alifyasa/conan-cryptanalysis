import re

def split_ciphertext(text, key_size):
    split_result = ["" for _ in range(key_size)]
    for idx, char in enumerate(text):
        split_result[idx % key_size] += char
    return split_result

def vigenere_decrypt_char(ciphertext_char, key_char):
    return chr(((ord(ciphertext_char) - ord(key_char)) % 26) + ord('A'))

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    for idx, ciphertext_char in enumerate(ciphertext):
        plaintext += vigenere_decrypt_char(ciphertext_char, key[idx % len(key)])
    return plaintext

def key_elimination(ciphertext, key_guess):
    shifted_ciphertext = ciphertext[key_guess:]
    difference = ""
    for idx, shifted_char in enumerate(shifted_ciphertext):
        difference += vigenere_decrypt_char(ciphertext[idx], shifted_char)
    return difference

def find_all_substring_indices(main_string, substring):
    return [m.start() for m in re.finditer(f'(?={substring})', main_string)]

def key_elimination_method(ciphertext, guess_words, guess_key_lengths):
    results = []
    for guess_key_length in guess_key_lengths:
        ciphertext_difference = key_elimination(ciphertext, guess_key_length)
        for guess_word in guess_words:
            guessed_plaintext_difference = key_elimination(guess_word, guess_key_length)
            substring_locations = find_all_substring_indices(ciphertext_difference, guessed_plaintext_difference)
            for substring_location in substring_locations:
                ciphertext_part = ciphertext[substring_location:substring_location + guess_key_length]
                guessed_plaintext_part = guess_word[:guess_key_length]
                guessed_key = vigenere_decrypt(ciphertext_part, guessed_plaintext_part)
                dencrypted_result = vigenere_decrypt(ciphertext, guessed_key)
                encrypted_result_idx = find_all_substring_indices(dencrypted_result, guess_word)
                if encrypted_result_idx:
                    results += [(
                        len(encrypted_result_idx), guess_word, guessed_key, dencrypted_result[:20]
                    )]
                    # print(ciphertext_part, guessed_plaintext_part, guessed_key, len(encrypted_result_idx))
                    # print(f"{guessed_key} -> {encrypted_result[:20]}")
    results.sort(key= lambda x: x[0], reverse=True)
    for result in results[:50]:
        print(result)

def frequency_analysis(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    freq_arr = []
    for (key, value) in freq.items():
        perc = value / len(text) * 100
        freq[key] = perc
        freq_arr += [(key, perc)]
    freq_arr.sort(key= lambda x: x[1], reverse=True)
    return freq_arr

def frequency_analysis_method(ciphertext, guess_key_lengths):
    key = ""
    for guess_key_length in guess_key_lengths:
        columns_ciphertext = split_ciphertext(ciphertext, guess_key_length)
        print(guess_key_length)
        for col in columns_ciphertext: 
            freq = frequency_analysis(col)
            key_char = vigenere_decrypt_char(freq[0][0], 'E')
            print(key_char, freq[:3])
            key += key_char
            # G -> E
            # G - E -> K
    print(key)


ciphertext = ""

with open("ciphertext.txt", "r") as f:
    ciphertext = ''.join(f.read().split())

guess_words = [
    "THE",
]

guess_key_lengths = [12]

if __name__ == "__main__":
    # key_elimination_method(ciphertext, guess_words, guess_key_lengths)    
    frequency_analysis_method(ciphertext, guess_key_lengths)