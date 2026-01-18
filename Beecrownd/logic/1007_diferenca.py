"""
==================================
    1007 - Diferença
==================================

Objetivo: 
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D 
segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada:
O arquivo de entrada contém 4 valores inteiros.

Saída:
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e 
depois da igualdade.

"""

# ==========================================
# Entrada: Declaração de Variáveis e Input de Dados
# ==========================================

valor_a = int(input())
valor_b = int(input())
valor_c = int(input())
valor_d = int(input())

# ==========================================
# Processamento: Formula para cálculo da diferença
# ==========================================

calculo_diferenca = (valor_a * valor_b - valor_c * valor_d)


# ==========================================
# Saída: dados calculados e formatados
# ==========================================
print("DIFERENCA = " + str(calculo_diferenca))