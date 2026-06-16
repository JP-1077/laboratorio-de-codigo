import sys
from pathlib import Path
from importlib import import_module


sys.path.insert(0, str(Path(__file__).parent.parent / 'app' / 'beecrownd' / 'ad-hoc'))


def teste_soma_mofiz_exemplo_1():
    modulo = import_module('1016_carrega_ou_nao_carrega')
    assert modulo.calcular_soma_mofiz(4,6) == 10

def teste_soma_mofiz_exemplo_2():
    modulo = import_module('1016_carrega_ou_nao_carrega')
    assert modulo.calcular_soma_mofiz(6,9) == 15