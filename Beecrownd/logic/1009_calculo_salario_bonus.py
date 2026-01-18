"""
==================================
    1009 - Salário com Bônus
==================================

Objetivo: 
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com 
duas casas decimais.

Entrada:
O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, 
representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

Saída:
Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

"""

# ==========================================
# Entrada: Declaração de Variáveis e Input de Dados
# ==========================================
nome_vendedor = input()
salario_vendedor = float(input())
total_vendas_final_mes = float(input())

# ==========================================
# Processamento: Formula para cálculo do salário
# ==========================================
calculo_recebimento_final_mes = salario_vendedor + (total_vendas_final_mes * 0.15)

# ==========================================
# Saída: dados calculados e formatados
# ==========================================
print("TOTAL = R$ {:.2f}".format(calculo_recebimento_final_mes))




