from pypraticot6.telefonista import Telefonista


def test_telefonista_init():
    assert Telefonista()


def telefonista():
    telefonista_ = Telefonista()
    telefonista_.adicionar('Rene', '2345678')
    telefonista_.adicionar('Raul', '4567896')
    return telefonista_


def test_adicionar_usuario():
    """Usuario pode ser adicionado com seu telefone"""
    assert [('Rene', '2345678'), ('Raul', '4567896')] == telefonista().usuarios


# teste de integração

def test_spam():
    ligacoes_para_usuarios = list(telefonista().spam())
    ligacoes_esperadas = [
        'Telefonista cadastro de Rene ligar para 2345678',
        'Telefonista cadastro de Raul ligar para 4567896',
    ]
    assert ligacoes_esperadas == ligacoes_para_usuarios
