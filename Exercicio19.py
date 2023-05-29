nota = int(input("Informe a nota do participante: "))

if nota <= 50:
    print ("Certificado de Participação")
elif nota <= 60:
        print ("Certificado de Menção Honrosa")
elif nota <= 70:
    print ("Medalha de Bronze")
elif nota <= 90:
    print ("Medalha de Prata")
else:
    print ("Medalha de Ouro")

    