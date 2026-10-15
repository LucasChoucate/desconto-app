from typing import TypedDict

from app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO


class PedidoViewModel(TypedDict):
    cliente: str
    valor_original: float
    valor_desconto: float
    valor_final: float
    tipo_desconto: str


class PedidoPresenter:
    def apresentar(self, output_dto: CriarPedidoOutputDTO) -> PedidoViewModel:
        return {
            "cliente": output_dto.cliente,
            "valor_original": output_dto.valor_original,
            "valor_desconto": output_dto.valor_desconto,
            "valor_final": output_dto.valor_final,
            "tipo_desconto": output_dto.tipo_desconto,
        }

    def apresentar_lista(
        self, output_dtos: list[CriarPedidoOutputDTO]
    ) -> list[PedidoViewModel]:
        lista_formatada = []

        for output_dto in output_dtos:
            pedido_formatado = self.apresentar(output_dto)
            lista_formatada.append(pedido_formatado)

        return lista_formatada
