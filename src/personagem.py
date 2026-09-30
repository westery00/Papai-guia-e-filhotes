from abc import ABC, abstractmethod


class Personagem(ABC):

    def __init__(self, nome, vida, ataque, defesa, vida_atual):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.vida_atual = vida

    def esta_vivo(self):
        return self.vida_atual > 0

    
    def receber_dano(self, dano):
        # TODO: calcular o dano considerando a defesa
        pass

    @abstractmethod
    def atacar(self, alvo):
        pass

    def mostrar_status(self):
        print(
            f"{self.nome} | "
            f"Vida: {self.vida_atual}/{self.vida} | "
            f"Ataque: {self.ataque} | "
            f"Defesa: {self.defesa}"
        )
