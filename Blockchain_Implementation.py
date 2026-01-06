import hashlib
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_contents = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(block_contents.encode()).hexdigest()


class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=previous_block.hash
        )

        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block):
        target = "0" * self.difficulty

        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Recalculate hash
            if current.hash != current.calculate_hash():
                return False

            # Check hash linking
            if current.previous_hash != previous.hash:
                return False

        return True



if __name__ == "__main__":                  # Example usage
    blockchain = Blockchain(difficulty=2)

    blockchain.add_block("First transaction")
    blockchain.add_block("Second transaction")
    blockchain.add_block("Third transaction")

    print("Blockchain valid:", blockchain.is_valid())

    for block in blockchain.chain:
        print(vars(block))
