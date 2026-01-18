"""
==================================
    1005 - Produto Simples
==================================

Objetivo: 
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. 
A seguir mostre a variável PROD com mensagem correspondente.   

Entrada:
O arquivo de entrada contém 2 valores inteiros.

Saída:
Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. 
Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation 
Error”.

"""

# ==========================================
# Entrada: Declaração de Variáveis e Input de Dados
# ==========================================
num_1 = int(input())
num_2 = int(input())

# ==========================================
# Processamento: Cálculo da Área do Círculo
# ==========================================
operacao_produto = num_1 * num_2

# ==========================================
# Saída: dados calculados e formatados
# ==========================================
print("PROD = " + str(operacao_produto))