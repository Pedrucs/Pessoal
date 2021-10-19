import random 

#INPUT DO JOGADOR (USUÁRIO)
user_action = input("Faça sua escolha (pedra, papel, tesoura: ") #para o usuário fazer a seleção, vai salvar a seleção em uma variável para depois

#FAZER A MÁQUINA ESCOLHER
possible_action = ["pedra", "papel", "tesoura"]
computer_action = random.choice(possible_action)

#MOSTRANDO A ESCOLHA DE AMBOS
print(f"\nVocê Escolheu {user_action}, A máquina escolheu {computer_action}.\n") 

#DETERMINANDO O VENCEDOR

if user_action == computer_action:
    print(f"Ambos os jogadores escolheram {user_action}. É um empate!")
elif user_action == "pedra":
    if computer_action == "tesoura":
        print("Pedra esmaga a tesoura! Você ganhou!")
    else:
        print("Papel cobre a pedra! Você perdeu :(")
elif user_action == "papel":
    if computer_action == "pedra":
        print("Papel cobre a pedra! Você ganhou!")
    else:
        print("Tesoura corta o papel! Você perdeu :(")
elif user_action == "tesoura":
    if computer_action == "pedra":
        print("Tesoura corta o papel! Você ganhou!")
    else:
        print("Pedra esmaga a tesoura! Você perdeu :(")




