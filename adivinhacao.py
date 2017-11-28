print("        P  /_\  P                              ")
print("       /_\_|_|_/_\                             ")
print("   n_n | ||. .|| | n_n         Bem vindo ao    ")
print("   |_|_|nnnn nnnn|_|_|     Jogo de Adivinhação!")
print("  |' '  |  |_|  |'  ' |                        ")
print("  |_____| ' _ ' |_____|                        ")
print("        \__|_|__/                              ")

numero_secreto = 43
chute = int(input("Digite o seu número: "))
print("Você digitou: ", chute)
if(chute == numero_secreto):
    print("Você acertou")
else:
    print("Você errou")