#View - o que vai aparecer para o usuario
usuario = input("Digite o nome de usuario: \n")
senha = input("Digite sua senha: \n")


#Model - Oque vem do banco de dados
usuario_DB = 'joao'
senha_DB = '123'

# Controller - A Validação entre o View e o Model.
if usuario == usuario_DB and senha == senha_DB:
    print("Pode Acessar")
else:
    print("Usuario ou Senha inválido!")