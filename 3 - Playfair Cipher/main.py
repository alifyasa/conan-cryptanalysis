from termcolor import colored
from enum import StrEnum, auto

class Color(StrEnum):
    RED = auto()
    GREEN = auto()

class DecryptStatus(StrEnum):
    SUCCESS = auto()
    MISSING = auto()

class DecryptAttempt:
    def __init__(self, data: str, status: DecryptStatus):
        self.data = data
        self.status = status

    def color(self):
        colors = {
            DecryptStatus.SUCCESS: Color.GREEN,
            DecryptStatus.MISSING: Color.RED
        }
        return colors[self.status]

    def __str__(self) -> str:
        return colored(self.data, self.color())

class PlayfairDecryptor:
    def __init__(self, key):
        self.key = key

    def create_index_dict(self):
        index_dict = {}
        for i, row in enumerate(self.key):
            for j, char in enumerate(row):
                index_dict[char] = (i, j)
        return index_dict

    def find_index(self, char):
        for i, row in enumerate(self.key):
            if char in row:
                return i, row.index(char)
        return None, None

    def decrypt(self, ciphertext):
        attempts = []
        index_dict = self.create_index_dict()
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        
        for pair in pairs:
            i1, j1 = index_dict.get(pair[0], (None, None))
            i2, j2 = index_dict.get(pair[1], (None, None))
            
            if i1 is None or i2 is None or j1 is None or j2 is None:
                attempts.append(DecryptAttempt(pair, DecryptStatus.MISSING))
            elif i1 == i2:
                fst_char = self.key[i1][(j1 - 1) % 5]
                snd_char = self.key[i2][(j2 - 1) % 5]
                if fst_char == "_" or snd_char == "_":
                    attempts.append(DecryptAttempt(pair, DecryptStatus.MISSING))
                else:
                    attempts.append(DecryptAttempt(fst_char + snd_char, DecryptStatus.SUCCESS))
            elif j1 == j2:
                fst_char = self.key[(i1 - 1) % 5][j1]
                snd_char = self.key[(i2 - 1) % 5][j2]
                if fst_char == "_" or snd_char == "_":
                    attempts.append(DecryptAttempt(pair, DecryptStatus.MISSING))
                else:
                    attempts.append(DecryptAttempt(fst_char + snd_char, DecryptStatus.SUCCESS))
            else:
                fst_char = self.key[i1][j2]
                snd_char = self.key[i2][j1]
                if fst_char == "_" or snd_char == "_":
                    attempts.append(DecryptAttempt(pair, DecryptStatus.MISSING))
                else:
                    attempts.append(DecryptAttempt(fst_char + snd_char, DecryptStatus.SUCCESS))
        
        return attempts

class Loader:
    def load_ciphertext(ciphertext_file = "ciphertext.txt"):
        with open(ciphertext_file, "r") as f:
            return ''.join(f.read().split())
    
    def load_key(key_file = "keys/key_final.txt"):
        with open(key_file, 'r') as f:
            # read first 5 lines
            lines = [next(f) for _ in range(5)]

        # Split each line into individual characters
        result = []
        for line in lines:
            characters = line.strip().split(' ')
            result.append(characters)
        
        return result

if __name__ == "__main__":
    key = Loader.load_key("keys/key_final.txt")

    decryptor = PlayfairDecryptor(key)

    ciphertext = Loader.load_ciphertext()

    results = decryptor.decrypt(ciphertext)
    print(''.join([str(i) for i in results]))