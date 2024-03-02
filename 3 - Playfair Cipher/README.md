# Playfair Cryptanalysis Attempt

Playfair deciphering attempt steps:
 1. Do frequency analysis on each pair of cipher character.
 2. Attempt to reconstruct the key by matching pair of cipher character with frequent pairs of english characters.

## How to Run

```
sudo docker run -it $(sudo docker build -q .)
```