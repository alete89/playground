import repoUsuarios as repo
from Usuario import Usuario
import RSAKeyHandle as rsa

keysize = 1024

usuarios =[
        Usuario("ale", rsa.getKeyPair(keysize).publickey()),
        Usuario("pedro", rsa.getKeyPair(keysize).publickey()),
        Usuario("carlos", rsa.getKeyPair(keysize).publickey()),
        Usuario("alice", rsa.getKeyPair(keysize).publickey()),
        Usuario("bob", rsa.getKeyPair(keysize).publickey())
    ]
repo.agregarUsuarios(usuarios)

rsa.exportKeyToFile(rsa.encryptRsaKey(usuarios[0].pubkey),"ale.pem")
print(repo.getUsernameList())
print(repo.getPubKeyFromUsername("ale"))