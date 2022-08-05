import vaga
import sympy as s

class Estacionamento(vaga.Vaga):
    vagas_de_carro = 5                                             # Número de vagas máxima para carros
    carro_para_vaga = 0                                            # Número de carros esperando para estacionar
    total_vagas_livres_carro = 5                                   # Número de vagas livres para carros
    carros_para_estacionar = s.Matrix([["FILA", "PLACA", "TIPO"]]) # Lista de carros esperando para estacionar
    fila_carro = 1                                                 # Número de chegada de um carro esperando para estacionar

    vagas_de_moto = vagas_de_carro + 5                             # Número de vagas máxima para motos (incluindo as vagas de carro)
    moto_para_vaga = 0                                             # Número de motos esperando para estacionar
    total_vagas_livres_moto = 5                                    # Número de vagas livres exclusivamente para motos
    motos_para_estacionar = s.Matrix([["FILA", "PLACA", "TIPO"]])  # Lista de motos esperando para estacionar
    fila_moto = 1                                                  # Número de chegada de um carro esperando para estacionar

    vagas = s.Matrix([["ID", "PLACA", "TIPO", "VAGA"]])            # Registro de identificação da vaga, se está livre ou ocupada por um carro
                                                                   # ou moto, e a respectiva placa do veículo estacionado

    def __init__(self, placa, tipo):
        super().__init__(placa, tipo)

    @classmethod
    def vagas_livres(cls):
        for vaga in range(1, 11):
            cls.vagas = cls.vagas.row_insert(11, s.Matrix([[vaga, s.nan, s.nan, "Livre"]]))

    @classmethod
    def registrar_veiculos(cls, placa, tipo):
        if tipo == "carro":
            for linha_matriz_carro in range(1, cls.vagas_de_carro + 1):
                if cls.vagas[linha_matriz_carro, 1].equals(s.nan):
                    cls.vagas[linha_matriz_carro, 1] = placa
                    cls.vagas[linha_matriz_carro, 2] = tipo
                    cls.vagas[linha_matriz_carro, 3] = "Ocupada"
                else:
                    continue
                break
        if tipo == "moto":
            for linha_matriz_moto in range(cls.vagas_de_carro + 1, cls.vagas_de_moto + 1):
                if cls.vagas[linha_matriz_moto, 1].equals(s.nan):
                    cls.vagas[linha_matriz_moto, 1] = placa
                    cls.vagas[linha_matriz_moto, 2] = tipo
                    cls.vagas[linha_matriz_moto, 3] = "Ocupada"
                    break
                elif cls.total_vagas_livres_moto == 0 and cls.carro_para_vaga == 0:
                    for linha_matriz_carro in range(1, cls.vagas_de_carro + 1):
                        if cls.vagas[linha_matriz_carro, 1].equals(s.nan):
                            cls.vagas[linha_matriz_carro, 1] = placa
                            cls.vagas[linha_matriz_carro, 2] = tipo
                            cls.vagas[linha_matriz_carro, 3] = "Ocupada"
                            break
                else:
                    continue
                break

    @classmethod
    def estacionar_carro(cls, placa, tipo):
        cls.carro_para_vaga += 1

        if cls.vagas_de_carro >= cls.total_vagas_livres_carro > 0 and cls.carro_para_vaga != 0:
            cls.registrar_veiculos(placa, tipo)
            cls.total_vagas_livres_carro -= 1
            cls.carro_para_vaga -= 1
        elif cls.total_vagas_livres_carro == 0 and cls.carro_para_vaga != 0:
            cls.carros_para_estacionar = cls.carros_para_estacionar.row_insert(3, s.Matrix([[cls.fila_carro, placa, tipo]]))
            cls.fila_carro += 1

    @classmethod
    def remover_carro(cls, placa, tipo):
        for linha_matriz_carro in range(1, cls.vagas_de_carro + 1):
            if cls.vagas[linha_matriz_carro, 1].equals(placa):
                cls.vagas[linha_matriz_carro, 1] = s.nan
                cls.vagas[linha_matriz_carro, 2] = s.nan
                cls.vagas[linha_matriz_carro, 3] = "Livre"
                cls.total_vagas_livres_carro += 1
                if cls.carro_para_vaga != 0 and cls.vagas[linha_matriz_carro, 1].equals(s.nan):
                    cls.vagas[linha_matriz_carro, 1] = cls.carros_para_estacionar[4]
                    cls.vagas[linha_matriz_carro, 2] = cls.carros_para_estacionar[5]
                    cls.vagas[linha_matriz_carro, 3] = "Ocupada"
                    cls.carros_para_estacionar.row_del(1)
                    cls.fila_carro -= 1
                    cls.carro_para_vaga -= 1
                    cls.total_vagas_livres_carro -= 1
                elif cls.carro_para_vaga == 0 and cls.moto_para_vaga != 0 and cls.vagas[linha_matriz_carro, 1].equals(s.nan):
                    cls.vagas[linha_matriz_carro, 1] = cls.motos_para_estacionar[4]
                    cls.vagas[linha_matriz_carro, 2] = cls.motos_para_estacionar[5]
                    cls.vagas[linha_matriz_carro, 3] = "Ocupada"
                    cls.motos_para_estacionar.row_del(1)
                    cls.moto_para_vaga -= 1
                    cls.total_vagas_livres_carro -= 1

    @classmethod
    def estacionar_moto(cls, placa, tipo):
        cls.moto_para_vaga += 1

        if cls.vagas_de_moto >= cls.total_vagas_livres_moto > 0 and cls.moto_para_vaga != 0:
            cls.registrar_veiculos(placa, tipo)
            cls.total_vagas_livres_moto -= 1
            cls.moto_para_vaga -= 1
        elif cls.total_vagas_livres_moto == 0 and cls.total_vagas_livres_carro != 0 and cls.carro_para_vaga == 0:
            cls.registrar_veiculos(placa, tipo)
            cls.total_vagas_livres_carro -= 1
            cls.moto_para_vaga -= 1
        elif cls.total_vagas_livres_moto == 0 and cls.total_vagas_livres_carro == 0:
            cls.motos_para_estacionar = cls.motos_para_estacionar.row_insert(3, s.Matrix([[cls.fila_moto, placa, tipo]]))
            cls.fila_moto += 1

    @classmethod
    def remover_moto(cls, placa, tipo):
        for linha_matriz_vaga in range(1, cls.vagas_de_moto + 1):
            if cls.vagas[linha_matriz_vaga, 1].equals(placa):
                cls.vagas[linha_matriz_vaga, 1] = s.nan
                cls.vagas[linha_matriz_vaga, 2] = s.nan
                cls.vagas[linha_matriz_vaga, 3] = "Livre"
                if linha_matriz_vaga >= cls.vagas_de_carro + 1: # Entre as vagas de moto
                    cls.total_vagas_livres_moto += 1
                    if cls.moto_para_vaga != 0 and cls.vagas[linha_matriz_vaga, 1].equals(s.nan):
                        cls.vagas[linha_matriz_vaga, 1] = cls.motos_para_estacionar[4]
                        cls.vagas[linha_matriz_vaga, 2] = cls.motos_para_estacionar[5]
                        cls.vagas[linha_matriz_vaga, 3] = "Ocupada"
                        cls.motos_para_estacionar.row_del(1)
                        cls.moto_para_vaga -= 1
                        cls.total_vagas_livres_moto -= 1
                elif linha_matriz_vaga < cls.vagas_de_carro + 1: # Entre as vagas de carro
                    if cls.vagas_de_carro != 0 and cls.vagas[linha_matriz_vaga, 1].equals(s.nan):
                        cls.vagas[linha_matriz_vaga, 1] = cls.carros_para_estacionar[4]
                        cls.vagas[linha_matriz_vaga, 2] = cls.carros_para_estacionar[5]
                        cls.vagas[linha_matriz_vaga, 3] = "Ocupada"
                        cls.carros_para_estacionar.row_del(1)
                        cls.carro_para_vaga -= 1
                        # cls.total_vagas_livres_carro -= 1
                    elif cls.carro_para_vaga == 0 and cls.vagas[linha_matriz_vaga, 1].equals(s.nan):
                        cls.vagas[linha_matriz_vaga, 1] = cls.motos_para_estacionar[4]
                        cls.vagas[linha_matriz_vaga, 2] = cls.motos_para_estacionar[5]
                        cls.vagas[linha_matriz_vaga, 3] = "Ocupada"
                        cls.motos_para_estacionar.row_del(1)
                        cls.moto_para_vaga -= 1

    @classmethod
    def imprimir_vagas(cls):
        for linha_matriz_vagas in range(0, len(cls.vagas), 4):
            print(f'{cls.vagas[linha_matriz_vagas]} \t {cls.vagas[linha_matriz_vagas + 1]} \t '
                  f'{cls.vagas[linha_matriz_vagas + 2]} \t {cls.vagas[linha_matriz_vagas + 3]} \n')

    @classmethod
    def imprimir_carros_esperando(cls):
        for linha_matriz_carros_esperando in range(0, len(cls.carros_para_estacionar), 3):
            print(
                f'{cls.carros_para_estacionar[linha_matriz_carros_esperando]} \t {cls.carros_para_estacionar[linha_matriz_carros_esperando + 1]} \t '
                f'{cls.carros_para_estacionar[linha_matriz_carros_esperando + 2]}\n')

    @classmethod
    def imprimir_motos_esperando(cls):
        for linha_matriz_motos_esperando in range(0, len(cls.motos_para_estacionar), 3):
            print(
                f'{cls.motos_para_estacionar[linha_matriz_motos_esperando]} \t {cls.motos_para_estacionar[linha_matriz_motos_esperando + 1]} \t '
                f'{cls.motos_para_estacionar[linha_matriz_motos_esperando + 2]}\n')

    @classmethod
    def estado_estacionamento(cls):
        Estacionamento.imprimir_vagas()

        print(f'Número de vagas livres para carros: {cls.total_vagas_livres_carro}\n'
              f'Número de vagas livres para motos: {cls.total_vagas_livres_moto}\n'
              f'Número de carros para estacionar: {cls.carro_para_vaga}\n'
              f'Número de motos para estacionar: {cls.moto_para_vaga}\n')

        if cls.carro_para_vaga != 0:
            print(f'---------FILA DE ESPERA PARA CARROS---------\n')
            Estacionamento.imprimir_carros_esperando()
            print("\n")

        if cls.moto_para_vaga != 0:
            print(f'---------FILA DE ESPERA PARA MOTOS---------\n')
            Estacionamento.imprimir_motos_esperando()
            print("\n")