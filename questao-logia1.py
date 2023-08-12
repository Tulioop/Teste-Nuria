# Questão 1: Faça um programa, em seguida, um programa que solicite a entrada de dois números, em seguida imprime na tela o quadrado do menor número e a raiz quadrada do maior número, se for possível.


import math

def calcular_quadrado(numero):
    return numero ** 2

def calcular_raiz_quadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return None

# Solicita a entrada de dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula e imprime o quadrado do menor número
quadrado_menor = calcular_quadrado(min(numero1, numero2))
print(f"O quadrado do menor número é: {quadrado_menor}")

# Calcula e imprime a raiz quadrada do maior número, se possível
maior_numero = max(numero1, numero2)
raiz_maior = calcular_raiz_quadrada(maior_numero)
if raiz_maior is not None:
    print(f"A raiz quadrada do maior número é: {raiz_maior}")
else:
    print("Não é possível calcular a raiz quadrada do maior número.")
