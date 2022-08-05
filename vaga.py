import estacionamento

class Vaga:
    def __init__(self, placa, tipo):
        self._placa = placa
        self._tipo = tipo

    def ocupar(self):
        if self._tipo == 'carro':
            carro = estacionamento.Estacionamento(self._placa, self._tipo)
            carro.estacionar_carro(self._placa, self._tipo)

        elif self._tipo == 'moto':
            moto = estacionamento.Estacionamento(self._placa, self._tipo)
            moto.estacionar_moto(self._placa, self._tipo)

    def desocupar(self):
        if self._tipo == 'carro':
            carro = estacionamento.Estacionamento(self._placa, self._tipo)
            carro.remover_carro(self._placa, self._tipo)

        elif self._tipo == 'moto':
            moto = estacionamento.Estacionamento(self._placa, self._tipo)
            moto.remover_moto(self._placa, self._tipo)
