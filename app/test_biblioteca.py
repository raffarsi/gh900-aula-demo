from biblioteca import LIVROS


def test_tem_livros():
    assert len(LIVROS) >= 3
