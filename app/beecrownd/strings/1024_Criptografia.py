"""
==================================
1024 - Criptografia
==================================

Objetivo:
Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. 
Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' 
vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da 
metade em diante, o resultado final deve ser “3# rvzgV”.


Entrada:
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.


Saída:
Para cada entrada, deve-se apresentar a mensagem criptografada.


"""


# ==========================================
# Processamento: criptografia da mensagem
# ==========================================
def criptografar_mensagem(mensagem):

    # ==========================================
    # Primeiro Processamento
    # ==========================================
    primeiro_processamento = ''.join(
        chr(ord(caractere) + 3) if caractere.isalpha() else caractere
        for caractere in mensagem
    )

    # ==========================================
    # Segundo Processamento
    # ==========================================
    segundo_processamento = primeiro_processamento[::-1]


    # ==========================================
    # Terceiro Processamento
    # ==========================================
    metade = len(segundo_processamento) // 2
    terceiro_processamento = ''.join(
        chr(ord(caractere) - 1) if i >= metade else caractere
        for i, caractere in enumerate(segundo_processamento)
    )

    return terceiro_processamento

# ==========================================
# Saidas: criptografar e imprimir a mensagem
# ==========================================

def main():
    qtd_casos_teste = int(input())
    casos_testes_linha = []

    for i in range(qtd_casos_teste):
        numero_linha_testes = int(input())
        linhas = [input() for i in range(numero_linha_testes)]
        casos_testes_linha.append(linhas)

    for caso_teste in casos_testes_linha:
        for linha in caso_teste:
            mensagem_criptografada = criptografar_mensagem(linha)
            print(mensagem_criptografada)

if __name__ == "__main__":
    main()


