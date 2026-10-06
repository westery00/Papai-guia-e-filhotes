from guerreiro import Guerreiro
from inimigo import Inimigo
from batalha import Batalha
from mago import Mago


def main():
    Nome = input("Digite o nome do seu personagem: ")
    classe = input("Escolha a classe do seu personagem(1-Guerreiro, 2-Mago): ")
    if classe == "1":
        classe = Guerreiro  
    elif classe == "2":
        classe = Mago
    else:
        print("Classe inválida. O personagem será um Guerreiro por padrão.")
        classe = Guerreiro
        
    jogador = classe(Nome)

    inimigo = Inimigo(
        nome="Goblin",
        vida=100,
        ataque=20,
        defesa=5
    )

    batalha = Batalha(jogador, inimigo)

    batalha.iniciar()


if __name__ == "__main__":
    main()
