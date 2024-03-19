# exercicio 1

i = 13
soma = 0
k = 0

while k < i:
    k += 1
    soma += k
print(soma)

# exercicio 2

n = input("digite um numero para verificar se existe na sequência: ")
n = int(n)
n1 = 0
n2 = 1
n3 = 0

# 0 1 1 2 3 5 8 13
while True:
    print(n3)
    n2 += n1
    n1 = n3
    if n1 == n:
        print("seu número existe na sequência.")
        break
    elif n1 > n:
        print("seu número não existe na sequencia.")
        break
    n3 = n2
...
# exercicio 3

# a) Resposta: 9 (numeros impares)
# b) Resposta: 128 (dobro)
# c) Resposta: 49 (numero + numero impar)
# d) Resposta: 100
# e) Resposta: 13 (sequencia de fibonacci)
# f) Resposta: 200 (numeros que começam com a letra D)

# exercicio 4

# Ligue um dos interruptores e espere um pouco. Desligue e ligue um segundo interruptor.
# Vá até a sala. A lâmpada desligada e quente corresponde ao primeiro interruptor, 
# a lâmpada acesa ao segundo e a lâmpada apagada e fria ao terceiro.

# exercicio 5

n = input('digite seu nome: ')
print(n[::-1])