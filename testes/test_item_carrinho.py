from ecommerce.categoria import Categoria
from ecommerce.produto import Produto
from ecommerce.item_carrinho import ItemCarrinho


class TestItemCarrinho:

    def setup_method(self) -> None:
        categoria = Categoria("Informática")
        self.produto = Produto("Tablet", 1299.99, 10, categoria)

    def test_cria_item_com_produto_e_quantidade(self) -> None:
        item = ItemCarrinho(self.produto, 2)
        assert item.produto is self.produto
        assert item.quantidade == 2    
        
    def teste_preco_no_momento_igual_preco_produto(self) -> None:
        item = ItemCarrinho(self.produto, 2)
        assert item.preco_no_momento == 1299.99
        
    def teste_preco_no_momento_fixo(self) -> None: 
        item = ItemCarrinho(self.produto, 2)
        assert item.preco_no_momento == 1299.99