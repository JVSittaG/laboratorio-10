CUPONS = {"DEZ": (10, 10000), "VINTE": (20, 30000)}


class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._desconto = 0
        self._minimo = 0

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")
        if not isinstance(quantidade, int) or quantidade < 1:
            raise ValueError("quantidade deve ser inteira e ao menos 1")
        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")
        self._desconto, self._minimo = CUPONS[codigo]

    @property
    def total(self):
        desconto = self._desconto if self._subtotal >= self._minimo else 0
        return self._subtotal * (100 - desconto) // 100
