class CriadorEntrega:
    def criar(self, origem: str, pedido) -> Entrega:
        if origem == "loja_central":
            return EntregaCorreios(pedido, gerar_codigo(), modalidade="SEDEX")
        elif origem == "centro_sul":
            return EntregaTransportadora(pedido, gerar_codigo(), transportadora="Transportadora Sul")
        elif origem == "marketplace":
            ...  # regra do parceiro