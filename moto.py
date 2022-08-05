import vaga
import estacionamento

class Moto(vaga.Vaga):
    def __init__(self, placa, tipo):
        super().__init__(placa, tipo)
        self.estacionado = " "

    def estacionar(self):
        if estacionamento.Estacionamento.total_vagas_livres_moto != 0:
            self.estacionado = "vaga de moto"
            print(f'\n\nMoto estacionada em {self.estacionado}\n')
        elif estacionamento.Estacionamento.total_vagas_livres_moto == 0 and estacionamento.Estacionamento.moto_para_vaga != 0:
            self.estacionado = "fila de espera"
            print(f'\n\nMoto em {self.estacionado}\n')

    def sair_da_vaga(self):
        self.estacionado = "retirada"
        if estacionamento.Estacionamento.moto_para_vaga == 0:
            print(f'\n\nMoto foi {self.estacionado} do estacionamento\n')
        else:
            print(f'\n\nMoto foi {self.estacionado} do estacionamento e moto em fila de espera foi estacionada\n')
