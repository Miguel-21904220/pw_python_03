import os


class Automovel:

    def __init__(self, capacidade, quantidade, consumo):
        self.capacidade = capacidade
        self.quantidade = quantidade
        self.consumo = consumo

    def combustivel(self):
        return self.quantidade

    def autonomia(self):
        return self.quantidade*100 / self.consumo

    def abastercer(self, capacidade_litros):
        if capacidade_litros > self.capacidade-self.consumo:
            raise os.error("nao pode encher mais")

        self.quantidade += capacidade_litros
        return self.autonomia()

    def percorrer(self, distanciaPercorrida):
        if distanciaPercorrida > self.autonomia():
            raise os.error(f"Não ha gasolina disponivel para {distanciaPercorrida} km")

        self.quantidade -= distanciaPercorrida * self.consumo / 100
        return self.autonomia()



if __name__ == "__main__":
    a = Automovel(10, 30, 23)
    print(a.percorrer(200))
