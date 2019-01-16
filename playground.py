import repoUsuarios as repo
from Usuario import Usuario
import RSAKeyHandle as rsa
import AesPlayground as aes

keysize = 1024

usuarios = [
    Usuario("ale", rsa.getKeyPair(keysize)),
    Usuario("pedro", rsa.getKeyPair(keysize)),
    Usuario("carlos", rsa.getKeyPair(keysize)),
    Usuario("alice", rsa.getKeyPair(keysize)),
    Usuario("bob", rsa.getKeyPair(keysize))
]
repo.agregarUsuarios(usuarios)

# rsa.exportKeyToFile(rsa.encryptRsaKey(usuarios[0].pubkey),"ale.pem")
# print(repo.getUsernameList())
# print(repo.getPubKeyFromUsername("ale"))

# Ale le envía un mensaje a Pedro
mensaje = "Un mensaje de prueba."
destination_pubkey = repo.getPubKeyFromUsername("pedro")
session_key = rsa.get_random_bytes(16)
cipher_rsa = rsa.PKCS1_OAEP.new(destination_pubkey)
enc_session_key = cipher_rsa.encrypt(session_key)  # lista para mandar a Pedro
aes.encryptBytesWithAesToFile(mensaje, session_key, "data_para_pedro.bin")
