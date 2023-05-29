salario = float(input("Informe o salário do funcionário: "))

if salario > 8.250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

print ("Seu salário atual é de: ",novo_salario)