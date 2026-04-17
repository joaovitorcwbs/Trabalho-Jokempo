import random

pedra = 1
tesoura = 2
papel = 3
print()
print("~~~ Bem-vindo ao Jokenpô ~~~")
print()
def jogar():
    while True:
        print("Qual modo você deseja jogar:")
        print("JxC (Jogador vs Computador)")
        print("JxJ (Jogador vs Jogador)")
        print("CxC (Computador vs Computador)")
        print()
        
        escolha_jogo = input("Qual modo você deseja jogar: ")
        if escolha_jogo == "JxC":
            while True:
                opcoes = ["1", "2", "3"]
                jogador = input("Digite qual sera a jogada (1-Pedra) (2-Papel) (3-Tesoura) digite somente o numero:")
                if jogador not in opcoes:
                    print("Opção invalida! tente novamente.")
                    return
                computador = random.choice(opcoes)

                if jogador == computador:
                    print("Empate!")
                elif (jogador == "1" and computador == "3") or (jogador == "2" and computador == "1") or (jogador == "3" and computador == "2"):
                    print("Você vendeu!")
                else:
                    print("O computador venceu!")
                print("Você digitou", jogador, "e o computador digitou", computador)

                continuar = input("Você quer continuar ou deseja parar ""digite s/n: ").lower()
                if continuar == "n":
                    print("Voltando ao inicio")
                    break
            escolher_modo = input("Você deseja trocar de modo ou sair" " " "digite s/n")
            if escolher_modo == "n":
                print("Encerrando jogo")
                break    
jogar()


    

