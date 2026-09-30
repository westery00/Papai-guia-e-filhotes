from personagem import Personagem


class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=120,
            ataque=20,
            defesa=15,
            vida_atual=120
        )
        

    def atacar(self, alvo):
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida_atual = self.vida_atual - (dano - self.defesa)
