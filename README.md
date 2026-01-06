# Core_Team_Task_1
Minimal Blockchain Implementation (Python)

Overview
This project is a simple blockchain implementation built from scratch to demonstrate
core blockchain concepts such as hashing, block chaining, immutability, and proof-of-work.



Block Structure
Each block contains the following fields:

- **index** – Position of the block in the blockchain
- **timestamp** – Time when the block was created
- **data** – Payload stored in the block
- **previous_hash** – SHA-256 hash of the previous block
- **nonce** – A number adjusted during mining (Proof-of-Work)
- **hash** – SHA-256 hash of all the above fields

The hash is calculated using:
```python
SHA256(index + timestamp + data + previous_hash + nonce)

