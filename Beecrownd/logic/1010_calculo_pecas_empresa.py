"""
==================================
1010 - Calculo de peças da empresa
==================================

Objetivo: 
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, 
o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada:
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 
casas decimais.

Saída:
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço 
após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

"""

# ==========================================
# Entrada: Leitura dos dados da primeira peça
# ==========================================
codigo_peca_1, quantidade_comprada_peca_1, valor_unitario_peca_1 = input().split()
codigo_peca_1 = int(codigo_peca_1)
quantidade_comprada_peca_1 = int(quantidade_comprada_peca_1)
valor_unitario_peca_1 = float(valor_unitario_peca_1)

# ==========================================
# Entrada: Leitura dos dados da segunda peça
# ==========================================
codigo_peca_2, quantidade_comprada_peca_2, valor_unitario_peca_2 = input().split()
codigo_peca_2 = int(codigo_peca_2)
quantidade_comprada_peca_2 = int(quantidade_comprada_peca_2)
valor_unitario_peca_2= float(valor_unitario_peca_2)

# ==========================================
# Processamento: Calculo para saber o valor 
# a pagar
# ==========================================
Calculo_valor_pagar = (quantidade_comprada_peca_1 * valor_unitario_peca_1) + \
                      (quantidade_comprada_peca_2  * valor_unitario_peca_2)

# ==========================================
# Saída: dados calculados e formatados
# ==========================================
print(f"VALOR A PAGAR: R$ {Calculo_valor_pagar:.2f}")