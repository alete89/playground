class Usuario:
    def __init__(self, username: str, key):
        self.username = username
        self.key = key

    def getPubkey(self):
        return self.key.publickey()
