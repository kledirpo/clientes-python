# View - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: \n")
    senha_digitado = input("Informe sua senha: \n")
    usuario_completo = [usuario_digitado, senha_digitado]
    return usuario_completo


def exibir_mensagem(texto):
    print("\n")
    print("####################################")
    print(texto)
    print("####################################")
    print("\n")

def menu():
    print("1 - Para cadastrar novo cliente")
    print("2 - Para listar todos os clientes")
    print("3 - Para sair \n")
    opcao = input("Digite a opção \n")
    return opcao

def cadastro_cliente():
    nome = input("Informe o nome: \n")
    telefone = input("Informe o telefone \n")
    cliente = [nome,telefone]
    return cliente