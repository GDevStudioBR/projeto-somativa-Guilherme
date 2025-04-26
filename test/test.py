import os
import shutil
import pytest
from unittest.mock import patch

from src.main import *


PASTA_CARTAS = "cartas"

@pytest.fixture(autouse=True)
def limpar_cartas():
    if os.path.exists(PASTA_CARTAS):
        shutil.rmtree(PASTA_CARTAS)
    os.makedirs(PASTA_CARTAS)
    yield
    shutil.rmtree(PASTA_CARTAS)

def test_cadastrar_carta():
    with patch("builtins.input", side_effect=["Carta Teste", "Mágica", "1000", "1000", "Descrição"]):
        cadastrar_carta()
    assert os.path.exists(os.path.join(PASTA_CARTAS, "Carta Teste.txt"))

def test_listar_cartas(capsys):
    open(os.path.join(PASTA_CARTAS, "Carta.txt"), "w").close()
    listar_cartas()
    saida = capsys.readouterr().out
    assert "- Carta.txt" in saida

def test_apagar_todas_as_cartas():
    open(os.path.join(PASTA_CARTAS, "Carta.txt"), "w").close()
    with patch("builtins.input", return_value="s"):
        apagar_todas_as_cartas()
    assert os.listdir(PASTA_CARTAS) == []
print('boa noite')