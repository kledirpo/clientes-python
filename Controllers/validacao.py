# Controller - A Validação entre o View e o Model.
import Models.banco as banco
def validar_login(usuario,senha):
   usuario_DB = banco.model_usuario() 
   senha_DB = banco.model_senha()
   if usuario == usuario_DB and senha == senha_DB:
        print("Pode Acessar")
   else:
        print("Usuario ou Senha inválido!")