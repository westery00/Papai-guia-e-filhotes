from src.guerreiro import Guerreiro
from src.item import Item


def test_guerreiro_esta_vivo():

    guerreiro = Guerreiro("Arthur")

    assert guerreiro.esta_vivo() is True


def test_item_nao_pode_ser_usado_com_valor_zero(capsys):
    item = Item("poção de vida", 0)
    guerreiro = Guerreiro("Arthur")
    vida_inicial = guerreiro.vida_atual

    item.usar(guerreiro)

    assert guerreiro.vida_atual == vida_inicial
    assert "Não há poções disponíveis" in capsys.readouterr().out


def test_personagem_recebe_dano():
    # TODO
    pass


def test_personagem_morre():
    # TODO
    pass


def test_guerreiro_ataca():
    # TODO
    pass
