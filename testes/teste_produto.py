from ecommerce.categoria import Categoria
from ecommerce.produto import Produto


class TestProduto:
    
    def setup_method(self) -> None:
        self.categoria = Categoria('informatica')
        
    def test_cria_produto_com_atributos(self) -> None:
        produto = Produto("Tablet", 1299.99, 10, self.categoria)
        assert produto.nome == "Tablet"
        assert produto.preco == 1299.99
        assert produto.quantidade_estoque == 10
        assert produto.categoria is self.categoria
        
    def test_se_produto_disponivel_com_estoque(self) -> None:
        produto = Produto("Tablet", 1299.99, 10, self.categoria)
        assert produto.esta_disponivel() is True
        
    def test_se_produto_disponivel_sem_estoque(self) -> None:
        produto = Produto("Tablet", 1299.99, 10, self.categoria)
        assert produto.esta_disponivel() is False
        
    def test_produto_indisponivel_com_estoque_negativo(self) -> None:
        produto = Produto("Tablet", 1299.99, 10, self.categoria)
        assert produto.esta_disponivel() is False
    
    def test_aplicar_desconto_valido(self) -> None:
        produto = Produto("Tablet", 1299.99, 10, self.categoria)
        produto.aplicar_desconto(10)
        assert produto.preco == 3150.0

    def test_aplicar_desconto_invalido_abaixo_de_zero(self) -> None:
        produto = Produto("Tablet", 1299.99, 10, self.categoria)
        try:
            produto.aplicar_desconto(-5)
            assert False, "Deveria ter erro"
        except ValueError:
            pass
        
    def test_aplicar_desconto_invalido_acima_cem(self) -> None:
        produto = Produto("Tablet", 1299.99, 10, self.categoria)
        try:
            produto.aplicar_desconto(110)
            assert False, "Deveria ter erro"
        except ValueError:
            pass