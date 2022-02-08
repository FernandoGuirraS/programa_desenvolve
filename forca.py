import random

def desenha_forca(index):
	desenhos = [
		" ____   \n"
		"|       \n"
		"|       \n"
		"|       \n"
		"|       \n",

		" ____   \n"
		"|   0   \n"
		"|       \n"
		"|       \n"
		"|       \n",

		" ____   \n"
		"|   0   \n"
		"|   |   \n"
		"|       \n"
		"|       \n",

		" ____   \n"
		"|   0   \n"
		"|   |   \n"
		"|    \  \n"
		"|       \n",

		" ____   \n"
		"|   0   \n"
		"|   |   \n"
		"|  / \  \n"
		"|       \n",

		" ____   \n"
		"|   0   \n"
		"|   |\  \n"
		"|  / \  \n"
		"|       \n",

		" ____   \n"
		"|   0   \n"
		"|  /|\  \n"
		"|  / \  \n"
		"|       \n"
	]

	print("\n")
	print(desenhos[index])
	print("\n")

def apresentacao_jogo():
	print("*********************");
	print("*** JOGO DA FORCA ***");
	print("*********************\n");

def carrega_palavra_secreta():
	palavras = []
	with open("palavras.txt", "r") as arquivo:
		for linha in arquivo:
			palavras.append(linha.strip().upper())

	ind = random.randrange(0, len(palavras))
	return palavras[ind]

def mensagem_derrota(palavra_secreta):
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

def mensagem_vitoria():
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

def jogar():
	apresentacao_jogo()

	palavra_secreta = carrega_palavra_secreta()

	palavra_chute = ["_" for letra in palavra_secreta]

	acertou = False;
	enforcou = False;
	acertos = 0
	erros = 0
	tentativas = 6 # quantidade de chutes para se enforcar
	letras_erradas = []

	print(palavra_chute)
	print("\n")

	desenha_forca(erros)

	while(acertou != True or enforcou != True):
		chute = input("Digite uma Letra: ");
		chute = chute.strip().upper(); # strip tira espaços excessivos e upper transforma letra em maiusculas
		
		if(chute in palavra_secreta):
			index = 0
			for letra in palavra_secreta:
				if(letra == chute):
					palavra_chute[index] = letra;
					acertos += 1;
				index += 1;

		else:
			erros +=1;
			letras_erradas.append(chute)
			print("Faltam ", tentativas - erros, " tentativas \n")
		
		print(palavra_chute);
		print("\n")
		desenha_forca(erros)
		print("Letras Erradas: ", letras_erradas)
		print("\n")

		if(erros == tentativas):
			mensagem_derrota(palavra_secreta)
			enforcou == True;
			break
		elif(acertos == len(palavra_secreta)):
			mensagem_vitoria()
			acertou == True;
			break

if(__name__ == "__main__"):
	jogar();