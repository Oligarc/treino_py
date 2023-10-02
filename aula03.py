from enum import Enum, auto
from dataclasses import dataclass

class Produtos(Enum):
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()

@dataclass
class Pedido:
    produto: Produtos
    quantidade: int

@dataclass
class Totalizacao:
    bobina: int = 0
    chapa: int = 0
    painel: int = 0

@dataclass
class TipoProduto:
    bobina: int = 0
    chapa: int = 0
    painel: int = 0

def totaliza_pedidos(pedido_cliente: list[Pedido]) -> Totalizacao:
    '''Recebe os pedidos e faz a soma da quantidade de acordo com o produto,
    retorna o total de produtos solicitados
    >>> totaliza_pedidos([Pedido(Produtos.BOBINA, 100), Pedido(Produtos.CHAPA, 50), Pedido(Produtos.BOBINA, 30), Pedido(Produtos.PAINEL, 20), Pedido(Produtos.CHAPA, 15), Pedido(Produtos.BOBINA, 17)])
    Totalizacao(bobina=147, chapa=65, painel=20)'''
    totalizador = Totalizacao()

    for itens in pedido_cliente:
        produto = itens.produto
        quantidade = itens.quantidade

        if produto == Produtos.BOBINA:
            totalizador.bobina += quantidade
        elif produto == Produtos.CHAPA:
            totalizador.chapa += quantidade
        elif produto == Produtos.PAINEL:
            totalizador.painel += quantidade

    return totalizador


