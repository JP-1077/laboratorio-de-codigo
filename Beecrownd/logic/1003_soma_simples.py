"""
==================================
    1003 - Soma Simples
==================================

Objetivo: 
Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. 
A seguir escrever o valor desta variável.

Entrada:
O arquivo de entrada contém 2 valores inteiros.

Saída:
Imprima a mensagem "SOMA" com todas as letras maiúsculas, com um espaço em branco antes e depois da igualdade seguido pelo 
valor correspondente à soma de A e B. Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, 
caso contrário, você receberá "Presentation Error".

"""

# ==========================================
# Entrada: Declaração de Variáveis e Input de Dados
# ==========================================

# Usuário insere os números inteiros que deseja que sejam somados.
num_1 = int(input())
num_2 = int(input())

# ==========================================
# Processamento: Cálculo da Área do Círculo
# ==========================================

# Cálculo de soma entre os dois valores inputados anteriormente
operacao_soma = num_1 + num_2

# ==========================================
# Saída: dados calculados e formatados
# ==========================================

# Converte o valor retornado da operacao_soma para string para conseguir
# concatenar texto com a saida da operação.
print("SOMA = " +  str(operacao_soma))