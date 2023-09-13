def miner_block(blockchain, new_block):
    while True:
        new_block.nonce += 1
        new_block.hash = new_block.generate_hash()
        # Ajuste o número de zeros para controlar a dificuldade.
        if new_block.hash[:1] == "0":
            blockchain.add_block(new_block)
            break
