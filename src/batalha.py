class Batalha:

    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def iniciar(self):

        print("=" * 40)
        print("        INÍCIO DA BATALHA")
        print("=" * 40)

        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():

            print("\n--- STATUS ---")
            self.jogador.mostrar_status()
            self.inimigo.mostrar_status()

            print("\n--- AÇÕES ---")
            print("1 - Atacar")
            if self.jogador.__class__.__name__ == "Mago":
                print("2 - Usar magia")
            else:
                print("2 - Usar item")
            print("3 - Fugir")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogador.atacar(self.inimigo)

            elif opcao == "2":
                if self.jogador.__class__.__name__ == "Mago":
                    print("\n--- MAGIAS ---")
                    print("1 - Bola de Fogo (Causa 40 de dano, custa 20 de mana)")
                    print("2 - Cura (Recupera 30 de vida, custa 15 de mana)")
                    print("3 - Recuperar Mana (Recupera 20 de mana, custa 10 de vida)")

                    magia = input("Escolha uma magia: ")

                    if magia == "1":
                        self.jogador.usar_magia(self.inimigo, "bola de fogo")
                    elif magia == "2":
                        self.jogador.usar_magia(self.jogador, "cura")
                    elif magia == "3":
                        self.jogador.usar_magia(self.jogador, "recuperar mana")
                    else:
                        print("Magia inválida.")
                        continue
                else:
                    print("\n--- ITENS ---")
                    for i, item in enumerate(self.jogador.inventario):
                        print(f"{i + 1} - {item.nome} (Quantidade: {item.valor})")

                    item_escolhido = input("Escolha um item: ")

                    try:
                        item_index = int(item_escolhido) - 1
                        if 0 <= item_index < len(self.jogador.inventario):
                            item = self.jogador.inventario[item_index]
                            item.usar(self.jogador)
                        else:
                            print("Item inválido.")
                            continue
                    except ValueError:
                        print("Opção inválida.")
                        continue

            elif opcao == "3":
                print("Você fugiu da batalha!")
                return

            else:
                print("Opção inválida.")
                continue

            if self.inimigo.esta_vivo():
                self.inimigo.atacar(self.jogador)

        if self.jogador.esta_vivo():
            print("\nParabéns! Você venceu a batalha!")
        else:
            print("\nVocê foi derrotado na batalha.")
