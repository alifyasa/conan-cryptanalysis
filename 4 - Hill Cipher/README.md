# Hill Cryptanalysis Attempt

Hill deciphering attempt steps:
 1. Using known plaintext, create a 3x3 matrix
 2. Use matrix inverse to find key

```
C = K * P

K ^ -1 * C = P

C * P ^ -1 = K
```

## How to Run

```
sudo docker run -it $(sudo docker build -q .)
```