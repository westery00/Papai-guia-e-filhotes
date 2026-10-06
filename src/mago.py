import guerreiro
from personagem import Personagem

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=80,
            ataque=30,
            defesa=5,
            vida_atual=80
        )

        self.mana = 100

    def receber_dano(self, dano):
        self.vida_atual = self.vida_atual - (dano - self.defesa)

    def atacar(self, alvo):
        alvo.receber_dano(self.ataque)

    def usar_magia(self, alvo, magia):
        if magia == "bola de fogo":
            alvo.receber_dano(40)
            self.mana -= 20

        if magia == "cura":
            self.vida_atual += 30
            self.mana -= 15

        if magia == "recuperar mana":
            self.mana += 20
            self.vida_atual -= 10

        if self.mana <= 0:
            print("O mago não possui mana suficiente.")
            return

        pass
