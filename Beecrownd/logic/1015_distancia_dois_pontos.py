"""
==================================
1015 - Distância entre Dois Pontos
==================================

Objetivo:
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e 
calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:
xd = √(x2 - x1)² + (y2 - y1)²

Entrada:
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e 
a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída:
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

"""
# ==========================================
# ENTRADA: LEITURA DOS VALORES DOS PONTOS
# ==========================================

# Utiliza o map e split para ler dados em uma única linha
x_1, y_1 = map(float, input().split())
x_2, y_2 = map(float, input().split())

# ==========================================
# PROCESSAMENTO: Função para calcular a distância 
# entre os pontos utilizando a formula fornecida
# ==========================================
def calcular_distancia_entre_dois_pontos(x_1, y_1, x_2, y_2):
    calculo_distancia = ((x_2-x_1)**2 + (y_2 - y_1)**2) ** 0.5
    return calculo_distancia


# ==========================================
# SAÍDA: IMPRIMIR O VALOR DA DISTÂNCIA ENTRE OS DOIS PONTOS
# ==========================================
print(f"{calcular_distancia_entre_dois_pontos(x_1, y_1, x_2, y_2):.4f}")