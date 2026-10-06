class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def usar(self, personagem):
        if self.valor <= 0:
            print("Não há poções disponíveis.")
            return

        if self.nome == "poção de vida":
            personagem.vida_atual += 30
            print(f"{personagem.nome} usou uma poção de vida e recuperou 30 de vida.")
            self.valor -= 1
    