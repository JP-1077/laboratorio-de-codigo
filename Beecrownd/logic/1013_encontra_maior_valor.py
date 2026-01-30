"""
==================================
1013 - O maior numero
==================================

Objetivo: 
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada:
O arquivo de entrada contém três valores inteiros.

Saída:
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

"""


numero_a, numero_b, numero_c = map(int, input().split())


def encontra_maior_numero (numero_a, numero_b, numero_c):
    maior_ab = (numero_a + numero_b + abs(numero_a - numero_b)) / 2
    maior_abc = (maior_ab + numero_c + abs(maior_ab - numero_c)) / 2
    return maior_abc

print(f"{encontra_maior_numero(numero_a, numero_b, numero_c):.0f} eh o maior")