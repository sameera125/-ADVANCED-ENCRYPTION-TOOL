# Advanced Encryption Tool

## Features
- AES-256 encryption (via Python's `cryptography` package)
- Simple GUI with file selector for encrypting/decrypting
- Auto key generation and saving

## Requirements
- Python 3.x
- cryptography library (`pip install cryptography`)

## How to Run
```bash
python main.py
```

## Notes
- Encrypted files end with `.enc`
- Decrypted files end with `.dec`
- Keep the `.key` file secure — it's required for decryption
