'''
4o) Escreva um código que receba um valor de login e um valor de senha. Caso os valores
estejam corretos, retornar ao usuário: “Você está logado”. Caso contrário, informar: “Login ou
senha incorretos”.
Defina um valor padrão para login e senha.
'''

login_sistema = "MATHEUS"
senha_sistema = "12345"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == login_sistema and senha_sistema == senha:
    print("Você está logado!")
else:
    print("Login ou senha incorretos!")