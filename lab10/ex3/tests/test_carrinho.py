import pytest
from carrinho import Carrinho


def test_carrinho_vazio():
    assert Carrinho().total == 0


def test_um_item():
    c = Carrinho()
    c.adicionar(2500)
    assert c.total == 2500


def test_item_com_quantidade():
    c = Carrinho()
    c.adicionar(2500, quantidade=2)
    assert c.total == 5000


def test_preco_zero_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().adicionar(0)


def test_cupom_dez_abaixo_do_minimo_sem_desconto():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")
    assert c.total == 5000


def test_cupom_desconhecido():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")


def test_item_depois_do_cupom_abaixo_do_minimo_sem_desconto():
    c = Carrinho()
    c.aplicar_cupom("DEZ")
    c.adicionar(1000)
    assert c.total == 1000


@pytest.mark.parametrize("subtotal, esperado", [(9999, 9999), (10000, 9000)])
def test_dez_na_fronteira_do_minimo(subtotal, esperado):
    c = Carrinho()
    c.adicionar(subtotal)
    c.aplicar_cupom("DEZ")
    assert c.total == esperado


def test_desconto_vale_quando_subtotal_chega_ao_minimo():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")
    c.adicionar(5000)
    assert c.total == 9000


def test_cupom_vinte():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("VINTE")
    assert c.total == 24000


def test_vinte_abaixo_do_minimo_sem_desconto():
    c = Carrinho()
    c.adicionar(29999)
    c.aplicar_cupom("VINTE")
    assert c.total == 29999


def test_vinte_substitui_dez():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("DEZ")
    c.aplicar_cupom("VINTE")
    assert c.total == 24000


def test_dez_substitui_vinte():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("VINTE")
    c.aplicar_cupom("DEZ")
    assert c.total == 27000


def test_quantidade_zero_rejeitada():
    with pytest.raises(ValueError):
        Carrinho().adicionar(2500, quantidade=0)


@pytest.mark.parametrize("quantidade", [1.5, "2"])
def test_quantidade_nao_inteira_rejeitada(quantidade):
    with pytest.raises(ValueError):
        Carrinho().adicionar(2500, quantidade=quantidade)


def test_quantidade_negativa_rejeitada():
    with pytest.raises(ValueError):
        Carrinho().adicionar(2500, quantidade=-1)


def test_quantidade_um_aceita():
    c = Carrinho()
    c.adicionar(2500, quantidade=1)
    assert c.total == 2500
