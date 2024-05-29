import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

class EncryptionHandler:
    def __init__(self, password):
        self.password = password
        self.salt = b'saltysalt'
        self.key = scrypt(self.password, self.salt, 32, N=2**14, r=8, p=1)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt(self, data):
        data = base64.b64decode(data.encode())
        nonce = data[:16]
        tag = data[16:32]
        ciphertext = data[32:]
        cipher = AES.new(self.key, AES.MODE_GCM, nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode()