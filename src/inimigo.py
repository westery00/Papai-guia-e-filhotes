from personagem import Personagem


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa,
            vida_atual=vida
        )

    def atacar(self, alvo):
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida_atual = self.vida_atual - (dano - self.defesa)
