# programa pra criptografar
# utiliza o módulo python de encriptação pyAesCrypt que usa AES256-CBC
# para encriptar e decriptar arquivos e streams binários.

#https://pypi.org/project/pyAesCrypt/


import pyAesCrypt


# Chave de encriptação
password = "porfavor-use-uma-longa-senha-aleatoria"

# encripta arquivo "data.txt" gerando arquivo "data.txt.aes" encriptado
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password)
