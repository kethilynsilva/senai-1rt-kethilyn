def maior (a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and c >= a:
        return b
    else:
        return c
    
resultado = maior (10.5, 7.2, 9.8)
print ("O maior numero é: ",resultado)