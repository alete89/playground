from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

unTexto = "Un mensaje de ejemplo.".encode("utf-8")
unaKey = RSA.generate(1024)


def encryptRsaKey(RsaKey, password):
    return RsaKey.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")


def exportKeyToFile(encryptedKey, path):
    with open(path, "wb") as file:
        file.write(encryptedKey)


def importKeyFromFile(path, password):
    encoded_key = open(path, "rb").read()
    return RSA.import_key(encoded_key, password)


def main():
    exportKeyToFile(encryptRsaKey(unaKey, "asd"), "encryptedKey.bin")
    print(importKeyFromFile("encryptedKey.bin", "asd").publickey().export_key())


if __name__ == "__main__":
    main()
