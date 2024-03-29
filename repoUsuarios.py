from Usuario import Usuario
import collections

listaDeUsuarios = []


def getNextId():
    return max((user.id for user in listaDeUsuarios), default=0) + 1


def agregarUsuarios(usuarios):
    if isinstance(usuarios, collections.Iterable):
        listaDeUsuarios.extend(usuarios)
    else:
        listaDeUsuarios.append(usuarios)


def getPubKeyFromUsername(username):
    return [user.getPubkey() for user in listaDeUsuarios if user.username == username][0]


def getUsernameList():
    return [user.username for user in listaDeUsuarios]


def filterByUsername(string):
    return [user.username for user in listaDeUsuarios if string in user.username]


def main():
    usuarios = [
        Usuario("ale", b"PUBALE"),
        Usuario("pedro", b"PUBPEDRO"),
        Usuario("carlos", b"PUBCARLOS"),
        Usuario("alice", b"PUBALICE"),
        Usuario("bob", b"PUBBOB")
    ]
    agregarUsuarios(usuarios)
    # print(getPubKeyFromUsername("alice"))
    print(filterByUsername("al"))


if __name__ == "__main__":
    main()
