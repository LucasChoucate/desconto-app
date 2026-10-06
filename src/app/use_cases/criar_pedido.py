from src.app.entities.pedido import Pedido
from src.app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium


class CriarPedido:
    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        tipo_desconto = tipo_desconto.lower()

        if tipo_desconto == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        return Pedido(cliente, valor_original, desconto)
