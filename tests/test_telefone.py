import pytest

from pypraticot6.telefone import Telefone

NUMEROS_VALIDOS = ['1258446', 26264466]

def test_telefone_init():
    assert (Telefone() is not None)

@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_ligar(numero):
    telefone = Telefone()
    assert 'ligar para ' + str(numero) == telefone.ligar(numero)
