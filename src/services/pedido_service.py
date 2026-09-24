from src.models.pedido import Pedido

class PedidoService:
    """Classe de servoço para processar pedido e aplicar descontos"""

    def __init__(self):
        self.pedidos=[]

    def adicionar_pedido(self,pedido:Pedido):
        self.pedidos.append(pedido)

    def processar_pedido(self):
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")