import random

print()
print(  "::::::::::::::::::::::::::::::::::::\n" 
        "::: ~~~ Bem-vindo ao Jokenpô ~~~ :::\n"
        "::::::::::::::::::::::::::::::::::::")
print()
print()

while True:
    print("Qual modo você deseja jogar:\n")
    print("JxC (Jogador vs Computador)")
    print("CxC (Computador vs Computador)")
    print("JxJ (Jogador vs Jogador)")
    print()

    escolha_jogo = input("Modo de Jogo: ")
    print()
    print()

    if escolha_jogo == "JxC":
        contador = 0
        placar1 = 0
        placar2 = 0
        placar3 = 0
        while True:
            jogador = int(input("Digite (1-Pedra) (2-Papel) (3-Tesoura): "))
            contador += 1

            if jogador not in [1, 2, 3]:
                print("Opção inválida! Tente novamente.")
                continue

            computador = random.randint(1, 3)

            if jogador == computador:
                print("=====================\n"
                        "       Empate!\n"
                        "=====================")
                placar3 += 1
                print()
                
            elif (jogador == 1 and computador == 3) or \
                 (jogador == 2 and computador == 1) or \
                 (jogador == 3 and computador == 2):
                
                print("=====================\n"
                        "   Você venceu!\n"
                        "=====================")
                print()
                placar1 += 1
            else:
                print("=====================\n"
                        "O computador venceu!\n"
                        "=====================")
                placar2 += 1
                print()

            print("Você:", jogador, "| Computador:", computador)
            print()
            print("#########################\n"
                f"        ROUND : {contador}          \n"
                    "#########################\n"
                f"    VOCÊ       : {placar1}\n"
                f"    COMPUTADOR : {placar2}\n"
                f"    EMPATES    : {placar3}\n"
                    "#########################")
            print()

            continuar = input("Continuar? (s/n): ").lower()
            if continuar == "n":
                break

    elif escolha_jogo == "CxC":
        contador = 0
        placar3 = 0
        placar2 = 0
        placar1 = 0
        while True:
            computador1 = random.randint(1, 3)
            computador2 = random.randint(1, 3)
            contador += 1

            if computador1 == computador2:
                print("=====================\n"
                        "       Empate!\n"
                        "=====================")
                placar3 += 1
                print()
            elif (computador1 == 1 and computador2 == 3) or \
                 (computador1 == 2 and computador2 == 1) or \
                 (computador1 == 3 and computador2 == 2):
                print("=====================\n"
                        "O computador 1 venceu!\n"
                        "=====================")
                placar1 += 1
                print()
            else:
                print("=====================\n"
                        "O computador 2 venceu!\n"
                        "=====================")
                placar2 += 1
                print()

            print("Comp1:", computador1, "| Comp2:", computador2)
            print()
            print("#########################\n"
                f"        ROUND : {contador}          \n"
                    "#########################\n"
                f"    COMPUTADOR 2 : {placar1}\n"
                f"    COMPUTADOR 1 : {placar2}\n"
                f"    EMPATES      : {placar3}\n"
                    "#########################")
            print()

            continuar = input("Continuar? (s/n): ").lower()
            if continuar == "n":
                break
    elif escolha_jogo == 'JxJ':
        print("Digite seu Nickname: ")
        print()
        name1 = input("Jogador 1: ")
        name2 = input("Jogador 2: ")
        placar1 = 0
        placar2 = 0
        placar3 = 0
        contador = 0
        print()
        while True:
            jogador1 = int(input(f"{name1} - Digite (1-Pedra) (2-Papel) (3-Tesoura): "))
            jogador2 = int(input(f"{name2} - Digite (1-Pedra) (2-Papel) (3-Tesoura): "))
            contador += 1
            if jogador1 == jogador1 == jogador2 :
                print("=====================\n"
                        "       Empate!\n"
                        "=====================")
                placar3 += 1
                print()
            elif (jogador1 == 1 and jogador2 == 3) or \
                 (jogador1 == 2 and jogador2 == 1) or \
                 (jogador1 == 3 and jogador2 == 2):
                print("=====================\n"
                        f" {name1} venceu!\n"
                        "=====================")
                placar1 += 1
                print()
            else:
                print("=====================\n"
                        f" {name2} venceu!\n"
                        "=====================")
                placar2 += 1
                print()
            print(name1,":", jogador1, name2,"| :", jogador2)
            print()
            print("#########################\n"
                f"        ROUND : {contador}          \n"
                    "#########################\n"
                f"        {name1} : {placar1}\n"
                f"        {name2} : {placar2}\n"
                f"        EMPATES : {placar3}\n"
                    "#########################")
            print()
            print()

            continuar = input("Continuar? (s/n): ").lower()
            if continuar == "n":
                break
    sair = input("Deseja sair do jogo? (s/n): ").lower()
    if sair == "s":
        print("Encerrando jogo...")
        break
