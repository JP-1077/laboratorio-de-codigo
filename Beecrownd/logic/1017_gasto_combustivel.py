"""
==================================
1017 - Gasto de Combustível
==================================

Objetivo:
Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. 
Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na 
viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular 
quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

Entrada:
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas) e o segundo é a velocidade média durante a 
mesma (em km/h).

Saída:
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

"""

tempo_gasto_viagem = int(input())
velocidade_media = int(input())

def calcular_gasto_combustivel(tempo_gasto_viagem, velocidade_media):
    calculo_distancia_percorrida = tempo_gasto_viagem * velocidade_media
    calculo_gasto_combustivel = calculo_distancia_percorrida / 12
    return calculo_gasto_combustivel

print(f"{calcular_gasto_combustivel(tempo_gasto_viagem, velocidade_media):.3f}")