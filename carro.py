import vaga
import estacionamento

class Carro(vaga.Vaga):
    def __init__(self, placa, tipo):
        super().__init__(placa, tipo)
        self.estacionado = " "

    def estacionar(self):
        if estacionamento.Estacionamento.total_vagas_livres_carro != 0:
            self.estacionado = "estacionado"
            print(f'\n\nCarro foi {self.estacionado}\n')
        elif estacionamento.Estacionamento.total_vagas_livres_carro == 0 and estacionamento.Estacionamento.carro_para_vaga != 0:
            self.estacionado = "fila de espera"
            print(f'\n\nCarro em {self.estacionado}\n')

    def sair_da_vaga(self):
        self.estacionado = "retirado"
        if estacionamento.Estacionamento.carro_para_vaga != 0:
            print(f'\n\nCarro foi {self.estacionado} e carro em fila de espera foi estacionado\n')
        # elif Estacionamento.carro_para_vaga == 0 and Estacionamento.moto_para_vaga != 0:
        #     print(f'\n\nCarro foi {self.estacionado} e moto em fila de espera foi estacionado em vaga de carro')
        elif estacionamento.Estacionamento.carro_para_vaga == 0 and estacionamento.Estacionamento.moto_para_vaga == 0:
            print(f'\n\nCarro foi {self.estacionado}')