from blockchain import Blockchain
from block import Block
from miner import miner_block


if __name__ == "__main__":
    minha_blockchain = Blockchain()

    for i in range(1, 4):
        novo_bloco = Block(i, f"Dados do Bloco {i}", "")
        miner_block(minha_blockchain, novo_bloco)


    print(minha_blockchain.is_valid())

    for bloco in minha_blockchain.chain:
        print(f"Índice: {bloco.index}")
        print(f"Timestamp: {bloco.timestamp}")
        print(f"Dados: {bloco.data}")
        print(f"Hash Anterior: {bloco.previous_hash}")
        print(f"Nonce: {bloco.nonce}")
        print(f"Hash: {bloco.hash}")
        print("\n")