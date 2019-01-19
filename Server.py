from Usuario import Usuario
import RSAKeyHandle as rsa
import repoUsuarios as repo

usuarios = [
    Usuario("ale", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("pedro", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("carlos", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("alice", rsa.getKeyPair(rsa.KEY_SIZE)),
    Usuario("bob", rsa.getKeyPair(rsa.KEY_SIZE))
]
repo.agregarUsuarios(usuarios)
