def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def encontrar_maior(a, b):
    if a > b:
        return a
    else:
        return b

def encontrar_menor(a, b):
    if a < b:
        return a
    else:
        return b

def exibir_menu():
    print("Menu:")
    print("a. Somar")
    print("b. Multiplicar")
    print("c. Maior número")
    print("d. Menor número")
    escolha = input("Escolha uma opção (a, b, c ou d): ")
    return escolha

def main(5):
