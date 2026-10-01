usuario = "surpresa"
senha = "12345"


loginusuario = input("Digite seu usuário: ")
loginsenha = input("Digite sua senha: ")

if loginusuario == usuario and loginsenha == senha:
    print("Você foi logado!")
else:
    print("Usuário ou senha incorretos!") 