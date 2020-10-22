import os

LOGIN_EMAIL = os.environ.get("USR_MAIL" )
SENHA_EMAIL = os.environ.get("PAS_MAIL")

print("Olá Mundo")
print(LOGIN_EMAIL, SENHA_EMAIL)