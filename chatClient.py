from ChatWindow import ChatWindow
from Usuario import Usuario
import RSAKeyHandle as rsa

username = input("Ingresá tu nombre de usuario")
current_user = Usuario(username, rsa.getKeyPair(rsa.KEY_SIZE))
# notificar al server un nuevo usuario online
