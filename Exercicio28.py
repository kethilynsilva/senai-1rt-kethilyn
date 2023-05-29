def area (comprimento, largura):
    area_terreno = comprimento * largura
    return area_terreno

comprimento = float(input("Indique o comprimento do terreno: "))
largura = float(input("Indique a largura do terreno: "))

resultado = area(comprimento, largura)
print ("A area do terreno é de: ",resultado,"metros quadrado")