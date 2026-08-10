from ecommerce.categoria import Categoria


class Produto: 
    
    def __init__(self, nome: str, preco: float, quantidade_estoque: int, categoria: Categoria ) -> None:
        self. nome = nome 
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.categoria = categoria
        
        
    def esta_disponivel(self) -> bool:
        return self.quantidade_estoque > 0
    
    def aplicar_desconto(self, percentual: float) -> None:
        if not 0 <= percentual <= 100:
            raise ValueError("O percentual deve estar entre 0 e 100%")
        self.preco -= self.preco - (self.preco * (percentual / 100))
        # self.preco = self.preco - self.preco * (percentual / 100)
        
    def alterar_preco(self, novo_preco: float) -> None:
        if novo_preco <= 0:
            raise ValueError("Preco deve ser positivo")
        self.preco = novo_preco
        
        if __name__  == '__main__':
            from ecommerce.categoria import Categoria
            
            cat = Categoria('Informatica')
            produto = Produto("Tablet", 1299.99, 10, cat)
            print(f"Produto: {produto.nome}, Preco: {produto.preco}, Em estoque: {produto.esta_disponivel()}")
        
            produto.aplicar_desconto(15)
            print(f"Produto: {produto.nome}, Preco: {produto.preco}, Em estoque: {produto.esta_disponivel()}")

            produto.alterar_preco(999.0)
            print(f"Produto: {produto.nome}, Preco: {produto.preco}, Em estoque: {produto.esta_disponivel()}")
