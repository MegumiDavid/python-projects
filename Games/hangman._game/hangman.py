import random

def jogar():

      print_abertura_jogo()

      palavra_secreta = carregar_palavra_secreta()

      letra_acertada = inicializar_letras_acertadas(palavra_secreta)


      #for letra in palavra_secreta:
            #letra_acertada.append('_')             o que foi feito em cima soq mais extenso

      enforcou = False
      acertou = False
      erros = 0

      while (not acertou and not enforcou):

            chute = pede_chute()



            if chute in palavra_secreta:
                  marca_chute_correto(chute, letra_acertada, palavra_secreta)
            else:
                  erros += 1
                  print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))
                  desenha_forca(erros)


            enforcou = erros == 8
            acertou = '_' not in letra_acertada

            print(letra_acertada)
            if (acertou):
                imprime_mensagem_vencedor()
                break
            #else:
                #imprime_mensagem_perdedor()



      print('***'*10,"Fim de jogo",'***'*10)

def print_abertura_jogo():
      print('***' * 10)
      print('Bem vindo ao jogo de forca')
      print('***' * 10)

def carregar_palavra_secreta():
      arquivo = open('palavras.txt', 'r')
      palavras = []

      for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

      numero = random.randrange(0, len(palavras))
      palavra_secreta = palavras[numero].upper()
      return palavra_secreta

      arquivo.close()

def inicializar_letras_acertadas(palavra):
      return ['_' for letra in palavra]

def pede_chute():
      chute = input('Qual a letra? ')
      chute = chute.strip().upper()
      return chute

def marca_chute_correto(chute, letra_acertada, palavra_secreta):
      index = 0
      for letra in palavra_secreta:
            if (chute == letra):
                  letra_acertada[index] = letra
            # [index] = [1] a posição
            index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
      print("Parabéns, você ganhou!")
      print("       ___________      ")
      print("      '._==_==_=_.'     ")
      print("      .-\\:      /-.    ")
      print("     | (|:.     |) |    ")
      print("      '-|:.     |-'     ")
      print("        \\::.    /      ")
      print("         '::. .'        ")
      print("           ) (          ")
      print("         _.' '._        ")
      print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
      jogar()