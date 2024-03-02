# Substitution Cryptanalysis

Cryptanalysis Steps:
 1. Use frequency analysis to determine popular characters, bigram, and trigrams.
 2. Substitute it with popular english characters, bigrams, and trigrams.
 3. Trial and Error. Try familiar english words.

## How to Run

```
sudo docker run -it $(sudo docker build -q .)
```