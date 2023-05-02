import forca
import advinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("informe o jogo: "))

if jogo != 1:
    print("jogando advinhação")
    advinhacao.jogar()

else:
    print("jogando forca")
    forca.jogar()