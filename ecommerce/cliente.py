from ecommerce.criador_notificacao import CanalNotificacao
from ecommerce.carrinho import Carrinho

class Cliente:
    
    def __init__(self, nome: str, email: str, telefone: str, canal_preferido: CanalNotificacao = CanalNotificacao.EMAIL) -> None:
        self.nome = nome
        self.email = email
        self.carrinho: Carrinho | None = None
        self.telefone = telefone
        self.canal_preferido = canal_preferido
        self._pedidos: list["Pedido"] = []
        
    @property
    def pedidos(self):
        return list(self._pedidos)
        
    def possui_carrinho(self) -> bool: 
        return self.carrinho is not None
    
    def finalizar_compra(self) -> "Pedido":
        if self.carrinho in None: 
            raise ValueError("Carrinho está Vazio")
        pedido = self.carrinho.finalizar()
        self._pedidos.append(pedido)
        self.carrinho.esvaziar()
        return pedido

    @property
    def contato(self) -> str:
        if self.canal_preferido == CanalNotificacao.SMS:
            return self.telefone
        return self.email

if __name__ == '__main__': 
    cliente = Cliente("Eduardo", "eduardo@gmail.com")
    print(f"Cliente: {cliente.nome}, Email: {cliente.email}")
    print(f"Possui carrinho: {cliente.possui_carrinho()}")