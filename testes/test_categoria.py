from ecommerce.categoria import Categoria


class TestCategoria:

    def test_cria_categoria_com_nome(self) -> None:
        categoria = Categoria("Informática")
        assert categoria.nome == "Informática"