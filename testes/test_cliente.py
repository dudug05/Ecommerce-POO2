from ecommerce.cliente import Cliente

class TesteCliente: 
    
    def test_cria_cliente_com_nome_e_email(self) -> None:
        cliente = Cliente("Eduardo", "Eduardo@gmail.com")
        assert cliente.nome == "Eduardo"
        assert cliente.email == "Eduardo@gmail.com"

    def test_cliente_sem_carrinho(self) -> None:
        cliente = Cliente("Eduardo", "Eduardo@gmail.com")
        assert cliente.possui_carrinho() is False