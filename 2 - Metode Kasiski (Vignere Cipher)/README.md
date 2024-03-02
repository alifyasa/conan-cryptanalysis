# Vigenere Cryptanalysis Attempt

Vigenere deciphering attempt steps:
 1. Guess the key length (for example, guessed 3).
 2. Split ciphertext (if ciphertext is ABCDEFGHI, split to [ADG, BEH, CFI]).
 3. Frequency analysis (Check frequency for each [ADG, BEH, CFI]. If it looked like english, the key length is probably correct).
 4. The problem become solving multiple Caesar Cipher. (Solve each of [ADG, BEH, CFI])
 5. Try decrypting. 
    - If failed, adjust the key and repeat.
    - If success, DONE. 

## How to Run

```
sudo docker run -it $(sudo docker build -q .)
```