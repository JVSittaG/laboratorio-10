from fila import Fila
import pytest


def test_fila_nova_nao_tem_senhas_aguardando():
    assert Fila().aguardando == 0


def test_primeira_normal_e_n1():
    assert Fila().emitir("normal") == "N1"


def test_segunda_normal_e_n2():
    f = Fila()
    f.emitir("normal")
    assert f.emitir("normal") == "N2"


def test_prioritaria_tem_numeracao_propria():
    f = Fila()
    f.emitir("normal")
    assert f.emitir("prioritaria") == "P1"


def test_tipo_invalido_lanca_value_error():
    with pytest.raises(ValueError):
        Fila().emitir("vip")


def test_aguardando_conta_senhas_emitidas():
    f = Fila()
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.aguardando == 2


def test_chamar_fila_vazia_lanca_index_error():
    with pytest.raises(IndexError):
        Fila().chamar()


def test_normais_seguem_ordem_de_chegada():
    f = Fila()
    f.emitir("normal")
    f.emitir("normal")
    assert f.chamar() == "N1"
    assert f.chamar() == "N2"


def test_chamar_reduz_aguardando():
    f = Fila()
    f.emitir("normal")
    f.emitir("normal")
    f.chamar()
    assert f.aguardando == 1


def test_prioritaria_passa_na_frente_da_normal():
    f = Fila()
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.chamar() == "P1"


def test_prioritarias_seguem_ordem_de_chegada():
    f = Fila()
    f.emitir("prioritaria")
    f.emitir("prioritaria")
    assert f.chamar() == "P1"
    assert f.chamar() == "P2"


def test_limite_de_duas_nao_vale_sem_normal_esperando():
    f = Fila()
    for _ in range(3):
        f.emitir("prioritaria")
    assert [f.chamar() for _ in range(3)] == ["P1", "P2", "P3"]


def test_normal_depois_de_duas_prioritarias_seguidas():
    f = Fila()
    f.emitir("normal")
    for _ in range(3):
        f.emitir("prioritaria")
    assert [f.chamar() for _ in range(4)] == ["P1", "P2", "N1", "P3"]


def test_contagem_zera_depois_de_chamar_normal():
    f = Fila()
    for _ in range(2):
        f.emitir("normal")
    for _ in range(5):
        f.emitir("prioritaria")
    esperado = ["P1", "P2", "N1", "P3", "P4", "N2", "P5"]
    assert [f.chamar() for _ in range(7)] == esperado
