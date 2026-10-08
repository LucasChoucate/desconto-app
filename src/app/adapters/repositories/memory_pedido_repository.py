from app.entities.pedido import Pedido
from app.gateways.pedido_gateway import IPedidoGateway
from app.frameworks.database.memory_database import MemoryDatabase


class MemoryPedidoRepository(IPedidoGateway):
    def __init__(self, database: MemoryDatabase):
        self.database = database

    def salvar(self, pedido: Pedido) -> None:
        self.database.pedidos.append(pedido)

    def listar(self) -> list[Pedido]:
        return self.database.pedidos
