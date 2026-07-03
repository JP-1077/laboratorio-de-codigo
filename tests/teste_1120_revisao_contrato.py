import sys
from pathlib import Path
from importlib import import_module
import pytest


sys.path.insert(0, str(Path(__file__).parent.parent / 'app' / 'beecrownd' / 'strings'))


def teste_revisao_contrato_teste_1():
    modulo = import_module('1120_revisao_contrato')
    assert modulo.encontrar_valor_contrato('3', '123456') == '12456'


def teste_revisao_contrato_teste_2():
    modulo = import_module('1120_revisao_contrato')
    assert modulo.encontrar_valor_contrato('5', '1500') == '100'

def teste_revisao_contrato_teste_3():
    modulo = import_module('1120_revisao_contrato')
    assert modulo.encontrar_valor_contrato('9', '23454324543423') == '23454324543423'


def teste_revisao_contrato_teste_4():
    modulo = import_module('1120_revisao_contrato')
    assert modulo.encontrar_valor_contrato('9', '99999999991999999') == '1'


def teste_revisao_contrato_teste_5():
    modulo = import_module('1120_revisao_contrato')
    assert modulo.encontrar_valor_contrato('5', '5000000') == '0'