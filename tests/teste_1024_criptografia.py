import sys
from pathlib import Path
from importlib import import_module
import pytest


sys.path.insert(0, str(Path(__file__).parent.parent / 'app' / 'beecrownd' / 'strings'))

def teste_criptografia_exemplo_1():
    modulo = import_module('1024_Criptografia')
    assert modulo.criptografar_mensagem("Texto #3") == "3# rvzgV"


def teste_criptografia_exemplo_2():
    modulo = import_module('1024_Criptografia')
    assert modulo.criptografar_mensagem("abcABC1") == "1FECedc"

def teste_criptografia_exemplo_3():
    modulo = import_module('1024_Criptografia')
    assert modulo.criptografar_mensagem("vxpdylY .ph") == "ks. \\n{frzx"

def teste_criptografia_exemplo_4():
    modulo = import_module('1024_Criptografia')
    assert modulo.criptografar_mensagem("vv.xwfxo.fd") == "gi.r{hyz-xx"