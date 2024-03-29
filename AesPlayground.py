from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

unaData = "Esta es la data que quiero encriptar".encode("utf-8")
unArchivo = "conAes.bin"
unaKey = get_random_bytes(24)  # 16, 24 o 32


def encryptBytesWithAesToFile(data:bytes, key, filename):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    file_out = open(filename, "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]

def encryptBytesWithAes(data:bytes, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return (cipher.nonce, tag, ciphertext)


def decryptBytesWithAesFromFile(filename, key):
    file_in = open(filename, "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

def decryptBytesWithAes(nonce_tag_ciphertext, key):
    nonce, tag, ciphertext = nonce_tag_ciphertext
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data


def main():
    encriptado = encryptBytesWithAes(unaData, unaKey)
    print(encriptado)
    print(decryptBytesWithAes(encriptado, unaKey))


if __name__ == "__main__":
    main()
