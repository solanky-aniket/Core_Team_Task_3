import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(text.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [Block(0, "Genesis Block", "0")]

    def add_block(self, data):
        prev = self.chain[-1]
        new_block = Block(len(self.chain), data, prev.hash)

        # Proof of Work (difficulty = 2)
        while not new_block.hash.startswith("00"):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            cur = self.chain[i]
            prev = self.chain[i - 1]

            if cur.hash != cur.calculate_hash():
                return False

            if cur.previous_hash != prev.hash:
                return False

        return True

    def show_chain(self):
        for block in self.chain:
            print("\n------------------------")
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("Nonce:", block.nonce)
        print("------------------------\n")


# -------- MENU SYSTEM --------

bc = Blockchain()

while True:
    print("\n====== SIMPLE BLOCKCHAIN MENU ======")
    print("1. Add new block")
    print("2. View blockchain")
    print("3. Check blockchain validity")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter data for new block: ")
        bc.add_block(data)
        print(" Block added successfully!")

    elif choice == "2":
        bc.show_chain()

    elif choice == "3":
        if bc.is_valid():
            print(" Blockchain is valid.")
        else:
            print(" Blockchain has been tampered!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print(" Invalid choice. Try again.")
