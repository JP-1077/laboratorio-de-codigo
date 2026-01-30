"""
==================================
1014 - Consumo de Combustível
==================================

Objetivo:
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de 
combustível gasto (em litros).

Entrada:
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), 
e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

Saída:
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

"""


valor_distancia_percorrida = int(input())
valor_combustivel_gasto = float(input())

calculo_consumo_medio_combustivel = valor_distancia_percorrida / valor_combustivel_gasto

print(f"{calculo_consumo_medio_combustivel:.3f} km/l")
