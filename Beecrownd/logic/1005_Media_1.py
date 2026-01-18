"""
==================================
    1005 - Média 1
==================================

Objetivo: 
Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a 
média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que 
cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada:
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída:
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço 
em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça 
de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

"""

# ==========================================
# Entrada: Declaração de Variáveis e Input de Dados
# ==========================================

# A entrada é a nota atribuidas ao aluno do tipo ponto flutuante (float)
nota_1 = float(input())
nota_2 = float(input())

# ==========================================
# Processamento: Cálculo da Média do Aluno
# ==========================================

# Primeiro calcula o peso das notas e depois divide pela soma dos pesos (11)
calculo_media = nota_1 * 3.5 + nota_2 * 7.5
media_final = calculo_media / 11


# ==========================================
# Saída: dados calculados e formatados
# ==========================================

# Resultado com 5 casas decimais após a virgula
print("MEDIA = {:.5f}".format(media_final))