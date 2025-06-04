from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    original_file_path = file_path.replace('.enc', '.dec')
    with open(original_file_path, 'wb') as dec_file:
        dec_file.write(decrypted)
