from Crypto.PublicKey import ECC

def generateNewKey():
    return ECC.generate(curve="secp256r1")

def importKeyFromFile(path, password=None):
    with open(path, "rt") as file:
        try:
            return ECC.import_key(file.read(), password)
        except ValueError as err:
            print(err)
            print("quizás la clave está encriptada?")
        

def exportKeyToFile(key:ECC.EccKey, path):
    with open(path, "wt") as file:
        file.write(key.export_key(format="PEM"))

def exportKeyToFileEncrypted(key:ECC.EccKey, path, password):
    with open(path, "wt") as file:
        file.write(key.export_key(format="PEM", passphrase=password, protection="PBKDF2WithHMAC-SHA1AndAES128-CBC"))


alice_priv = generateNewKey()
# bob_priv = generateNewKey()

# exportKeyToFile(alice_priv, "alice_priv.pem")
# exportKeyToFile(bob_priv, "bob_priv.pem")

# imported_alice_priv = importKeyFromFile("alice_priv.pem")
# exportKeyToFile(imported_alice_priv, "alice_priv2.pem")

# imported_bob_priv = importKeyFromFile("bob_priv.pem")

# alice_public = imported_alice_priv.public_key()
# bob_public = imported_bob_priv.public_key()

# exportKeyToFile(alice_public, "alice_public.pem")
# exportKeyToFile(bob_public, "bob_public.pem")

exportKeyToFileEncrypted(alice_priv, "alice_encrypted_private.pem","asd123")
alice_importada = importKeyFromFile("alice_encrypted_private.pem", "asd123")
