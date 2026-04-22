import random

print()
print("~~~ Bem-vindo ao Jokenpô ~~~")
print()

while True:
    print("Qual modo você deseja jogar:")
    print("JxC (Jogador vs Computador)")
    print("CxC (Computador vs Computador)")
    print()

    escolha_jogo = input("Qual modo você deseja jogar: ")

    if escolha_jogo == "JxC":
        while True:
            jogador = int(input("Digite (1-Pedra) (2-Papel) (3-Tesoura): "))

            if jogador not in [1, 2, 3]:
                print("Opção inválida! Tente novamente.")
                continue

            computador = random.randint(1, 3)

            if jogador == computador:
                print("Empate!")
            elif (jogador == 1 and computador == 3) or \
                 (jogador == 2 and computador == 1) or \
                 (jogador == 3 and computador == 2):
                print("Você venceu!")
            else:
                print("O computador venceu!")

            print("Você:", jogador, "| Computador:", computador)

            continuar = input("Continuar? (s/n): ").lower()
            if continuar == "n":
                break

    elif escolha_jogo == "CxC":
        while True:
            computador1 = random.randint(1, 3)
            computador2 = random.randint(1, 3)

            if computador1 == computador2:
                print("Empate!")
            elif (computador1 == 1 and computador2 == 3) or \
                 (computador1 == 2 and computador2 == 1) or \
                 (computador1 == 3 and computador2 == 2):
                print("Computador 1 venceu!")
            else:
                print("Computador 2 venceu!")

            print("Comp1:", computador1, "| Comp2:", computador2)

            continuar = input("Continuar? (s/n): ").lower()
            if continuar == "n":
                break

    sair = input("Deseja sair do jogo? (s/n): ").lower()
    if sair == "s":
        print("Encerrando jogo")
        break