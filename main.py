#View - o que vai aparecer para o usuario
def view():
    usuario = input("Digite o nome de usuario: \n")
    senha = input("Digite sua senha: \n")
    controller(usuario, senha)


#Model - O que vem do banco de dados
def model_usuario():
    usuario_DB = 'joao'
    return usuario_DB

def model_senha():
    senha_DB = '123'
    return senha_DB

# Controller - A Validação entre o View e o Model.
def controller(usuario,senha):
   usuario_DB = model_usuario() 
   senha_DB = model_senha() 
   if usuario == usuario_DB and senha == senha_DB:
        print("Pode Acessar")
   else:
        print("Usuario ou Senha inválido!")


# Chama a função principal que irá aparecer para o usuario
view()