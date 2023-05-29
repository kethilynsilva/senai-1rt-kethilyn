distancia = float(input("Informe a distância da viagem: "))

precomaior = distancia * 0.50
precomenor = distancia * 0.45

if distancia >= 200:
    print ("O valor da sua viagem será de: ",precomaior)
else:
    print ("O valor da sua viagem será de: ",precomenor)