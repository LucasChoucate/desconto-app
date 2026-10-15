from typing import ClassVar

from app.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP, IDesconto


class DescontoFactory:
    _descontos: ClassVar[dict[str, type[IDesconto]]] = {
        "normal": DescontoNormal,
        "vip": DescontoVIP,
        "premium": DescontoPremium,
    }

    @classmethod
    def criar(cls, tipo_desconto: str) -> IDesconto:
        tipo_normalizado = tipo_desconto.lower().strip()
        desconto = cls._descontos.get(tipo_normalizado)

        if desconto is None:
            raise ValueError("Tipo de desconto inválido")

        return desconto()

    @classmethod
    def registrar(cls, nome: str, desconto: type[IDesconto]) -> None:
        cls._descontos[nome.lower().strip()] = desconto