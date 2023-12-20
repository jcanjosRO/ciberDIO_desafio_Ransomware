
# programa pra decriptografar
# utiliza o módulode encriptação pyAesCrypt que usa AES256-CBC
# para encriptar e decriptar arquivos e streams binários.
#https://pypi.org/project/pyAesCrypt/

import pyAesCrypt
from os import stat, remove


password = "porfavor-use-uma-longa-senha-aleatoria"


try:
# decripta arquivo "data.txt.aes" gerando arquivo "dataout.txt" decriptografado e igual ao arquivo origianl "data.txt"
    
    pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password)

except ValueError:
        # remove arquivo de saida em caso de erro
        remove("dataout.txt")
