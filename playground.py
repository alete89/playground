import repoUsuarios as repo
from Usuario import Usuario
import RSAKeyHandle as rsa
import AesPlayground as aes


usuarios = [
    Usuario("ale", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("pedro", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("carlos", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("alice", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("bob", rsa.getKeyPair(rsa.KEY_SIZE))
]
repo.agregarUsuarios(usuarios)

# rsa.exportKeyToFile(rsa.encryptRsaKey(usuarios[0].pubkey),"ale.pem")
# print(repo.getUsernameList())
# print(repo.getPubKeyFromUsername("ale"))

# Ale le envía un mensaje a Pedro
mensaje = "Un mensaje de prueba.".encode("utf-8")
destination_pubkey = repo.getPubKeyFromUsername("pedro")
session_key = rsa.get_random_bytes(16)
cipher_rsa = rsa.getNewRsaCipher(destination_pubkey)
enc_session_key = cipher_rsa.encrypt(session_key)  # lista para mandar a Pedro
encrypted_data = aes.encryptBytesWithAes(mensaje, session_key)  # listo para mandar a Pedro

# Pedro: (tiene: enc_session_key y encrypted_data)
pedro_private = usuarios[1].key
cipher_rsa_pedro = rsa.getNewRsaCipher(pedro_private)
session_key_pedro = cipher_rsa_pedro.decrypt(enc_session_key)

data = aes.decryptBytesWithAes(encrypted_data, session_key_pedro)

print(data)
