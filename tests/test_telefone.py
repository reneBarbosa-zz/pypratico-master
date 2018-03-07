import pytest

from pypraticot6.telefone import Telefone
from pypraticot6.telefone import RediscarExcecao

NUMEROS_VALIDOS = ['1258446', 2345678]

def test_telefone_init():
    assert (Telefone() is not None)

@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_ligar(numero):
    telefone = Telefone()
    assert 'ligar para ' + str(numero) == telefone.ligar(numero)


@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_rediscar(numero):
    telefone = Telefone()
    telefone.ligar(numero)
    assert 'ligar para ' + str(numero) == telefone.rediscar()


@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_rediscar_dois_telefones_diferentes(numero):
    telefone = Telefone()
    telefone.ligar(numero)
    outro_telefone = Telefone()
    outro_numero = str(numero) + '1'
    outro_telefone.ligar(outro_numero)
    assert 'ligar para ' + str(numero) == telefone.rediscar()
    assert 'ligar para ' + str(outro_numero) == outro_telefone.rediscar()

def test_rediscar_excecao():
    '''certificar que rediscar antes de fazer ligação lança execeção'''
    telefone = Telefone()
    try:
        telefone.rediscar()
    except RediscarExcecao:
        pass #deu certo
    else:
        pytest.fail('Rediscar deveria ter lançado execeção')
