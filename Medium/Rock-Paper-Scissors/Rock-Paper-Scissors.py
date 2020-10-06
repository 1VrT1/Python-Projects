from random import choice

player = {'name': input('Enter your name: '), 'rating': 0}
print("Hello, " + player['name'])
with open('rating') as inf:  #
    for line in inf:
        line = line.strip().split()
        if player['name'] in line:
            player['rating'] = int(line[1])
# game rules - {Parameter : Parameters that can beat this parameter}
params, game_rules = input('Enter your parameters(Example - rock,paper,scissors):').split(','), {}
if len(params) < 3:
    params = ['rock', 'paper', 'scissors']
for i in params:
    ind, _ = params.index(i), []
    if ind == 0:
        _ += params[ind + 1:]
    elif ind == len(params) - 1:
        _ += params[:ind]
    else:
        _ += params[ind + 1:]
        _ += params[:ind]
    if len(_) % 2 != 0:
        game_rules[i] = _[:len(_) // 2]
    else:
        game_rules[i] = _[:len(_) // 2]
print('Okay, let\'s start')
while True:
    player_move = input()
    computer = choice(params)
    if player_move == '!exit':
        print('Bye!')
        break
    elif player_move == '!rating':
        print('Your rating:', player['rating'])
        continue
    elif player_move not in params:
        print('Invalid input')
        continue
    elif player_move == computer:
        print(f'There is a draw ({player_move})')
        player['rating'] += 50
    elif computer not in game_rules[player_move]:
        print(f'Well done. Computer chose {computer} and failed')
        player['rating'] += 100
    else:
        print('Sorry, but computer chose ' + computer)
