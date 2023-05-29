while True :
    numero = int(input("informe um numero: ")) 
    if numero < 0:
        print ("Programa encerrado.")
        if numero % 2 == 0:
            print ("É um numero par.")
        else:
            print ("É um numero impar.")
