import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC_PATH = ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from app.adapters.controllers.pedido_controller import PedidoController
from app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from app.frameworks.database.memory_database import MemoryDatabase
from app.presenters.pedido_presenter import PedidoPresenter
from app.use_cases.criar_pedido import CriarPedido


def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido_use_case, presenter)

    pedido1 = controller.criar_pedido("Cliente 1", 100.0, "normal")
    pedido2 = controller.criar_pedido("Cliente 2", 100.0, "vip")
    pedido3 = controller.criar_pedido("Cliente 3", 100.0, "premium")

    print("Pedidos criados:")
    print(pedido1)
    print(pedido2)
    print(pedido3)

    print("\nLista de pedidos:")
    print(controller.listar_pedidos())


if __name__ == "__main__":
    main()