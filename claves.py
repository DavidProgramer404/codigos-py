#creame en python  un gestor de claves aleatorios y robustos?

import secrets
import string

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password

    def add_password(self, name, password=None):
        if name in self.passwords:
            return "Name already exists. Please choose a different name."
        if not password:
            password = self.generate_password()
        self.passwords[name] = password
        return f"La clave generada {name} a sido creada."

    def get_password(self, name):
        if name not in self.passwords:
            return "Name not found. Please add it first."
        return self.passwords[name]

    def delete_password(self, name):
        if name not in self.passwords:
            return "Name not found. Please check and try again."
        del self.passwords[name]
        return f"La clave generada  {name} a sido eliminada."

# Usage
pm = PasswordManager()
print(pm.add_password(""))
print(pm.get_password(""))
