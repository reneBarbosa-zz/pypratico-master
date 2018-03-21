import pytest

from pypraticot6 import tel

def test_telefonista_init():
    """Telefonista possui inicializador vazio"""
    assert tel.Telefonista()


class TelefoneMock:
    def ligar(self, numero):
        return f'ligar de mentira para {numero}'


@pytest.fixture
def telefonista():
    telefonista_ = tel.Telefonista()
    telefonista_.adicionar('Rene', '2345678')
    telefonista_.adicionar('Raul', '4567896')
    return telefonista_


@pytest.fixture
def telefonista_fake(telefonista):
    telefonista.telefone = TelefoneMock


def test_adicionar_usuario(telefonista):
    """Usuario pode ser adicionado com seu telefone"""
    assert [('Rene', '2345678'),
            ('Raul', '4567896')] == telefonista.usuarios


# teste de integração
def test_spam_unitario(telefonista_fake):
    ligacoes_para_usuarios = list(telefonista_fake.spam())
    ligacoes_esperadas = [
        'Telefonista cadastro de Rene ligar de mentira para 2345678',
        'Telefonista cadastro de Raul ligar de mentira para 4567896',
    ]
    assert ligacoes_esperadas == ligacoes_para_usuarios


def test_spam_intergracao(telefonista):
    ligacoes_para_usuarios = list(telefonista.spam())
    ligacoes_esperadas = [
        'Telefonista cadastro de Rene ligar para 2345678',
        'Telefonista cadastro de Raul ligar para 4567896',
    ]
    assert ligacoes_esperadas == ligacoes_para_usuarios
