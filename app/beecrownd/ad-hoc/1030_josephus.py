"""
==================================
1027 - A lenda de Flavious Josephus
==================================

Objetivo:
O problema de Josephus é assim conhecido por causa da lenda de Flavius Josephus, um historiador judeu que viveu no século 1. 
Segundo o relato de Josephus do cerco de Yodfat, ele e seus companheiros (40 soldados) foram presos em uma caverna, cuja saída foi bloqueada pelos romanos. 
Eles preferiram suicidar-se a serem capturados, e decidiram que iriam formar um círculo e começar a matar-se pulando de três em três. Josephus afirma que, 
por sorte ou talvez pela mão de Deus, ele permaneceu por último e preferiu entregar-se aos romanos a suicidar-se.


Entrada:
Haverá NC (1 ≤ NC ≤ 30 ) casos de teste. Em cada caso de teste de entrada haverá um par de números inteiros positivos n (1 ≤ n ≤ 10000 ) e k (1 ≤ k ≤ 1000). 
O  número n representa a quantidade de pessoas no círculo, numeradas de 1 até n. 
O número k representa o tamanho do salto de um homem até o próximo homem que será morto.


Saída:
Para cada caso de teste de entrada será apresentada uma linha de saída no seguinte formato: Case n: m tendo sempre um espaço antes do n e do m.



Exemplo de Entrada	Exemplo de Saída
3                       Case 1: 3
5 2                     Case 2: 1
6 3                     Case 3: 25
1234 233 



-
"""

def josephus(n, k):
    sobrevivente = 0

    for i in range(1, n + 1):
        sobrevivente = (sobrevivente + k) % i

    return sobrevivente + 1


qtd_casos = int(input())

for caso in range(1, qtd_casos + 1):
    n, k = map(int, input().split())

    resultado = josephus(n, k)

    print(f"Case {caso}: {resultado}")



