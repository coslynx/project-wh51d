import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

class EncryptionUtils:
    def __init__(self, password):
        self.password = password
        self.salt = b'saltysalt'
        self.kdf = scrypt
        self.key = self.derive_key()

    def derive_key(self):
        return self.kdf(self.password, self.salt, 32, N=2**14, r=8, p=1)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt(self, encrypted_data):
        encrypted_data = base64.b64decode(encrypted_data)
        nonce = encrypted_data[:16]
        tag = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]
        cipher = AES.new(self.key, AES.MODE_GCM, nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode()