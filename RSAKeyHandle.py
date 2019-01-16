from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

import AesPlayground

unTexto = "Un mensaje de ejemplo.".encode("utf-8")

def getKeyPair(size:int):
    return RSA.generate(size)


def encryptRsaKey(RsaKey, password=None):
    return RsaKey.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")


def exportKeyToFile(encryptedKey, path):
    with open(path, "wb") as file:
        file.write(encryptedKey)


def importKeyFromFile(path, password=None):
    encoded_key = open(path, "rb").read()
    return RSA.import_key(encoded_key, password)


def exampleSender():
    recipient_key = importKeyFromFile("public.pem")
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    AesPlayground.encryptBytesWithAesToFile(unTexto, session_key, "encrypted_data_aes.bin")

    # Also export enc_session_key for the receiver
    exportKeyToFile(enc_session_key, "enc_sess_key.key")


def exampleReceiver():
    file_in = open("encrypted_data_aes.bin", "rb")
    my_private = importKeyFromFile("private.pem", "asd")
    enc_sess_key = open("enc_sess_key.key", "rb").read()
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]  # my_private.size_in_bytes(),

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(my_private)
    session_key = cipher_rsa.decrypt(enc_sess_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print(data.decode("utf-8"))


def main():
    # prev:
    # exportKeyToFile(encryptRsaKey(unaKey, "asd"), "private.pem")
    # exportKeyToFile(encryptRsaKey(unaKey.publickey()), "public.pem")

    # sender:
    # exampleSender()
    # receiver:
    # exampleReceiver()
    asd = getKeyPair(1024)
    pub = asd.publickey()
    print(pub)


if __name__ == "__main__":
    main()
