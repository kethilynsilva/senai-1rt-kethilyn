num = int(input("Digite um numero inteiro: "))
print ("A tabuada de ",num,"é: ")

for i in range (1,11):
 resultado = num * i
 print (num, "X", i, "=",resultado)