import random
print("Olá, Bem Vindo!")
num_jogos = int(input("Quantos jogos você gostaria de gerar? "))

for i in range(num_jogos):
    numeros = []

    while len(numeros) < 6:
        numero = random.randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
    
    print("Segue abaixo os jogos solicitados:")
    print(sorted(numeros))