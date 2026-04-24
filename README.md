Jokenpô em Python
=
Este projeto consiste na implementação do jogo clássico Pedra, Papel e Tesoura, desenvolvido em Python para a disciplina de Raciocínio Algorítmico.

O sistema funciona via terminal e permite diferentes modos de jogo, com controle de rodadas e placar.



Funcionalidades
-
O programa oferece três modos de jogo:

(JxC) Jogador vs Computador 

(CxC) Computador vs Computador 

(JxJ) Jogador vs Jogador

#Cada modalidade de jogo executa várias rodadas em sequência, permitindo que o jogador continue jogando até decidir encerrar a partida.
-

Resultado da rodada

Escolhas dos jogadores

Placar atualizado

Número da rodada


Regras do Jogo
-
As regras seguem o padrão clássico:

Pedra vence Tesoura

Tesoura vence Papel

Papel vence Pedra

Em caso de escolhas iguais, ocorre empate.


Como executar
-
Certifique-se de ter o Python instalado
Execute o arquivo principal:

python jokenpo.py

Escolha o modo de jogo digitando:
JxC
CxC
JxJ


Fluxo do Programa
-
1- Exibe menu inicial
2- Usuário escolhe modo
3- O jogo inicia com rodadas contínuas
4- A cada rodada:
    Jogadas são coletadas
    Resultado é exibido
    Placar é atualizado
5- Usuário decide continuar ou encerrar
6- Ao sair, o programa finaliza


Exemplo de execução
-
Exemplo de saída no terminal:

Qual modo você deseja jogar:

JxC (Jogador vs Computador)
CxC (Computador vs Computador)
JxJ (Jogador vs Jogador)

Modo de Jogo: #aqui você digita o modo de jogo
Modo de Jogo: JxC

Digite (1-Pedra) (2-Papel) (3-Tesoura): 1 #Digitei 1 por exemplo

Você: 1 | Computador: 1

#########################

        ROUND : 1   
        
#########################

    VOCÊ       : 0
    
    COMPUTADOR : 0
    
    EMPATES    : 1
    
#########################

Continuar? (s/n): n 

#Caso digite "s" o jogo ira continuar iniciando uma nova rodada, caso digite "n" o jogo irá fazer o seguinte passo:

Deseja sair do jogo? (s/n): n 

#Se você digitar "s" ele irá retornar ao menu de escolha de modo, se digitar "s" ele fara o seguinte passo:

Encerrando jogo... 

#E o jogo se encerrara, se quiser começar denovo terá que executar o comando python jokenpo.py denovo.


Estrutura do Código
-
O código utiliza:

  while para repetição do jogo
  if/elif/else para regras
  random.randint() para jogadas automáticas
  Variáveis para controle de placar e rodadas


Autores
-
João Vitor Chaves Venâncio

Victor Hugo dos Santos de Camargo

Vinicius Roxadelli de Almeida
