"""
==================================
    1008 - Calculo Salario
==================================

Objetivo: 
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula 
o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada:
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas 
trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída:
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. 
No caso do salário, também deve haver um espaço em branco após o $.

"""
# ==========================================
# Entrada: Declaração de Variáveis e Input de Dados
# ==========================================
numero_funcionario = int(input())
qtd_horas_trabalhadas = int(input())
valor_funcionario_horas_trabalhadas = float(input())

# ==========================================
# Processamento: Formula para cálculo do salário
# ==========================================
calculo_salario_funcionario =  qtd_horas_trabalhadas * valor_funcionario_horas_trabalhadas

# ==========================================
# Saída: dados calculados e formatados
# ==========================================
print("NUMBER = " + str(numero_funcionario))
print("SALARY = U$ {:.2F}" .format(calculo_salario_funcionario))