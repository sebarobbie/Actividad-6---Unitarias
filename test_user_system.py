
# --- CASOS DE USO ---
# Caso 1: Registro de usuario
# El sistema debe permitir registrar un nuevo usuario con nombre, correo y contraseña válidos.
# Caso 2: Inicio de sesión
# El usuario debe poder iniciar sesión con credenciales válidas.

# --- IMPLEMENTACIÓN DE FUNCIONES SIMPLES ---

class UserSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, name, email, password):
        if email in self.users:
            raise ValueError("El usuario ya está registrado.")
        if not email or "@" not in email:
            raise ValueError("Correo electrónico inválido.")
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        self.users[email] = {
            'name': name,
            'password': password
        }
        return True

    def login_user(self, email, password):
        if email not in self.users:
            raise ValueError("Usuario no registrado.")
        if self.users[email]['password'] != password:
            raise ValueError("Contraseña incorrecta.")
        return True

# --- PRUEBAS UNITARIAS CON PYTEST ---

import pytest

# Instancia para pruebas
@pytest.fixture
def user_system():
    return UserSystem()

# Pruebas del registro de usuario
def test_register_valid_user(user_system):
    assert user_system.register_user("Juan", "juan@example.com", "secure123") == True

def test_register_existing_user(user_system):
    user_system.register_user("Juan", "juan@example.com", "secure123")
    with pytest.raises(ValueError, match="El usuario ya está registrado."):
        user_system.register_user("Juan", "juan@example.com", "secure123")

def test_register_invalid_email(user_system):
    with pytest.raises(ValueError, match="Correo electrónico inválido."):
        user_system.register_user("Maria", "mariaexample.com", "password123")

def test_register_short_password(user_system):
    with pytest.raises(ValueError, match="La contraseña debe tener al menos 6 caracteres."):
        user_system.register_user("Carlos", "carlos@example.com", "123")

# Pruebas del inicio de sesión
def test_login_valid_user(user_system):
    user_system.register_user("Ana", "ana@example.com", "password123")
    assert user_system.login_user("ana@example.com", "password123") == True

def test_login_invalid_email(user_system):
    with pytest.raises(ValueError, match="Usuario no registrado."):
        user_system.login_user("no_existe@example.com", "password123")

def test_login_wrong_password(user_system):
    user_system.register_user("Luis", "luis@example.com", "password123")
    with pytest.raises(ValueError, match="Contraseña incorrecta."):
        user_system.login_user("luis@example.com", "wrongpass")
