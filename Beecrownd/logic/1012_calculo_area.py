"""
==================================
1012 - Área
==================================

Objetivo: 
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada:
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída:
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem 
correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto 
decimal.

"""

# ==========================================
# ENTRADA: LEITURA DOS VALORES A, B e C
# ==========================================
valor_a = float(input().strip().replace(',','.'))
valor_b = float(input().strip().replace(',','.'))
valor_c = float(input().strip().replace(',','.'))


# ==========================================
# PROCESSAMENTO: FUNÇÃO QUE CALCULA AS ÁREAS
# ==========================================
def calculo_area (valor_a, valor_b, valor_c):
    area_triangulo = (valor_a * valor_c) / 2
    area_circulo = 3.14159 * valor_c**2
    area_trapezio = ((valor_a + valor_b) * valor_c) / 2
    area_quadrado = valor_b**2
    area_retangulo = valor_a * valor_b

    return area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo

# ==========================================
# SAÍDAS DEMONSTRAÇÃO DOS RESULTADOS
# ==========================================
print(f"TRIANGULO: {calculo_area(valor_a, valor_b, valor_c)[0]:.3f}")
print(f"CIRCULO: {calculo_area(valor_a, valor_b, valor_c)[1]:.3f}")
print(f"TRAPEZIO: {calculo_area(valor_a, valor_b, valor_c)[2]:.3f}")
print(f"QUADRADO: {calculo_area(valor_a, valor_b, valor_c)[3]:.3f}")
print(f"RETANGULO: {calculo_area(valor_a, valor_b, valor_c)[4]:.3f}")