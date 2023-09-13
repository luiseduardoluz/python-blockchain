import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        dados_concatenados = str(self.index) + str(self.timestamp) + \
            str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(dados_concatenados.encode()).hexdigest()
