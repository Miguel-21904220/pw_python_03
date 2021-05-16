from Carro import Automovel


def main():
    global distancia
    opcao = 0
    combustivel = 60
    quantidade_combustivel = 10
    consumo = 15
    carro = Automovel(combustivel, quantidade_combustivel, consumo)

    while opcao != 2:
        print("0 - Abastecer")
        print("1 - Autonomia")
        print("2 - Distancia a Percorrer")
        print("3 - Exit")

        opcao = eval(input("-> "))

        if opcao == 0:
           consumo = int(input("Introduza a quantidade em litros: "))
        if opcao == 2:
            distancia = int(input("Introduza a distancia em km: "))
        if opcao == 3:
            return

        test = {
            0: carro.autonomia(),
            1: carro.autonomia(),
            2: carro.percorrer(distancia)
        }


if __name__ == "__main__":
    main()