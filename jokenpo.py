import random
turns_total= int(input('Digite o número de rodadas que quer jogar: '))
turns = 1;
plays = ['pedra', 'papel', 'tesoura']
player_1_wins = 0;
player_2_wins = 0;
while player_1_wins < turns_total/2 and player_2_wins < turns_total /2 and turns <= turns_total:
    print(f'Rodada atual: {turns}')
    play1 = input('Digite sua escolha: pedra, papel ou tesoura: ').lower()
    play2 = random.choice(plays)
    print(f'Escolha do computador: {play2}')
    if play1 == play2:
        print('Empate! Essa rodada não será contabilizada.')
    elif play1 == 'pedra' and play2 == 'tesoura' or play1 == 'papel' and play2 == 'pedra' or play1 == 'tesoura' and play2 == 'papel': 
        print('Player1 ganhou')
        turns += 1
        player_1_wins += 1
    else: 
        print('Computador ganhou')
        turns +=1
        player_2_wins += 1
      
if player_1_wins > player_2_wins:
    print('Player 1 é o vencedor!')
else:
    print('Player 2 é o vencedor!')
    #teste do git