class Fila:
    def __init__(self):
        self._numeros = {"normal": 0, "prioritaria": 0}
        self._normais = []
        self._prioritarias = []
        self._seguidas = 0

    def emitir(self, tipo):
        if tipo not in self._numeros:
            raise ValueError("tipo invalido")
        self._numeros[tipo] += 1
        senha = f"{tipo[0].upper()}{self._numeros[tipo]}"
        if tipo == "normal":
            self._normais.append(senha)
        else:
            self._prioritarias.append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self._normais) + len(self._prioritarias)

    def chamar(self):
        if self._prioritarias and (self._seguidas < 2 or not self._normais):
            self._seguidas += 1
            return self._prioritarias.pop(0)
        self._seguidas = 0
        return self._normais.pop(0)
