# Affine Cryptanalysis Attempt

Affine deciphering attempt steps:
 1. Using known plaintext (JPG magic byte), find a and b.

## How to Run

```
sudo docker run -it -v $(pwd):/app/flag $(sudo docker build -q .)
```