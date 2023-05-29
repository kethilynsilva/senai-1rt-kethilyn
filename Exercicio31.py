def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(verificar_par(4))   # Saída: True
print(verificar_par(7))   # Saída: False
print(verificar_par(0))   # Saída: True
print(verificar_par(11))  # Saída: False