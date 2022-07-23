import models.banco as banco
import views.formulario as view


# Controller - a validação
def validar_login(usuario_completo):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    if usuario_completo[0] == usuario_BD and usuario_completo[1] == senha_BD:
        #Após o login exibe uma mensagem e apresenta a função opcoes_menu
        view.exibir_mensagem("Usuario Autenticado com Sucesso")
        opcoes_menu()
    else:
        view.exibir_mensagem("Usuario ou Senha inválido")
        iniciar()


def iniciar():
    #Pega os valores recebidos na função formulario_login e manda para a função validar_login
    validar_login(view.formulario_login())
    ## Maneira mais leiga abaixo
    # usuario_completo = view.formulario_login()
    # validar_login(usuario_completo)

def opcoes_menu():
    opcao = view.menu()
    if opcao == '1':
        print("Cadastro de clientes")
        cadastrar_cliente()
    elif opcao == '2':
        print("Listagem de clientes")
    else:
        view.exibir_mensagem("Sistema Finalizado")
        exit()


def cadastrar_cliente():
    cliente = view.cadastro_cliente()

