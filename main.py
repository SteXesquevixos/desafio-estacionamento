import estacionamento
import vaga
import carro
import moto

if __name__ == '__main__':
    estacionamento.Estacionamento.vagas_livres()

    while True:
        estacionamento.Estacionamento.estado_estacionamento()
        placa = input("Placa: ")
        tipo = input("Tipo de veículo [carro/moto]: ")
        ocupar_ou_desocupar = input("Você deseja estacionar ou retirar o veículo da vaga? [ocupar/desocupar] ")

        veiculo = vaga.Vaga(placa, tipo)

        if ocupar_ou_desocupar == "ocupar":
            veiculo.ocupar()

            if tipo == "carro":
                carro.Carro(placa, tipo).estacionar()
            elif tipo == "moto":
                moto.Moto(placa, tipo).estacionar()

        elif ocupar_ou_desocupar == "desocupar":
            veiculo.desocupar()

            if tipo == "carro":
                carro.Carro(placa, tipo).sair_da_vaga()
            elif tipo == "moto":
                moto.Moto(placa, tipo).sair_da_vaga()

        elif placa == '' and tipo == '':
            break
