#View - o que vai aparecer para o usuario
from Controllers.validacao import validar_login

import Controllers.validacao as validacao
def formulario_login():
    usuario = input("Digite o nome de usuario: \n")
    senha = input("Digite sua senha: \n")
    validacao.validar_login(usuario, senha)