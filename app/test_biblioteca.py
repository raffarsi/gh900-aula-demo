from biblioteca import LIVROS, buscar_por_autor


def test_tem_livros():
    assert len(LIVROS) >= 3


def test_buscar_por_autor():
    assert buscar_por_autor("machado") == [LIVROS[0]]


def test_buscar_por_autor_sem_resultados():
    assert buscar_por_autor("autor inexistente") == []
