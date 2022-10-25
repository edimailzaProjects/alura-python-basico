import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("ESCOLHA O SEU JOGO")
    print("*********************************")

    print("[1]Forca ou [2] Adivinhação")

    jogo = int(input("Escolha seu jogo: "))

    if jogo ==1:
        print("Forca")
        forca.jogar_forca() #métodos sempre têm () e sua chamada é pelo nome do arquivo importado seguido de .
    elif jogo ==2:
        print("Adivinhacao")
        adivinhacao.jogar_adivinhacao() #estrutura do método "def nome_do_metodo():"


if(__name__=="__main__"):
    escolhe_jogo()