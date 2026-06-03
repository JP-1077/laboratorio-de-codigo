"""
==================================
1019 - Conversão de Tempo
==================================

Objetivo:
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o 
expresso no formato horas:minutos:segundos.

Entrada:
O arquivo de entrada contém um valor inteiro N.


Saída:
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Saída:
556 = 0:9:16

"""

import datetime

duracao_evento_segundos = int(input())

def conversao_tempo_hora (duracao_evento_segundos):
    conversao = str(datetime.timedelta(seconds = duracao_evento_segundos))
    return conversao

print((conversao_tempo_hora (duracao_evento_segundos)))