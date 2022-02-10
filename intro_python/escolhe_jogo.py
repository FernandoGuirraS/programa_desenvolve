import advinhacao
import forca

def escolhe_jogo():
	print("************************")
    print("**** ESCOLHA O JOGO ****")
    print("************************\n")

    print("***********************")
    print("\t(1) FORCA", "\t(2) ADVINHAÇÃO", sep="\n")
    print("***********************")
    op = int(input("OPÇÃO: "))

    if (op == 1):
    	forca.jogar()
    elif (op == 2):
    	advinhacao.jogar()

if (__name__ == "__main__"):
   	escolhe_jogo()