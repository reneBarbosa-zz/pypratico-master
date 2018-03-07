import pytest

from pypraticot6.telefone import Telefone

NUMEROS_VALIDOS = ['1258446', 2345678]

def test_telefone_init():
    assert (Telefone() is not None)

@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_ligar(numero):
    telefone = Telefone()
    assert 'ligar para ' + str(numero) == telefone.ligar(numero)

@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_rediscar():
    telefone = Telefone()
    numero_anterior = '2345678'
    telefone.ligar(numero_anterior)
    assert 'ligar para ' + str(numero_anterior) == telefone.rediscar()

def test_rediscar_dois_telefones_diferentes(numero):
    telefone = Telefone()
    telefone.ligar(numero)
    telefone2 = Telefone()
    outro_numero = str(numero) + '1'
    telefone2.ligar(outro_numero)
    assert 'ligar para ' + str(outro_numero) == telefone.rediscar()