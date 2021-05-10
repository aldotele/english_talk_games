import os
import base64
 

input_file = input('write the input file to use: ')
while True:
    try:
        inf = open(os.path.join('files', input_file))
        break
    except FileNotFoundError:
        input_file = input('file not found, please rewrite: ')


players = int(input("How many players? "))
players_list = []
scores = dict()

for p in range(players):
    player_name = input("Player's name: ")
    unique = f"{player_name}_{p}"
    players_list.append(unique)
    scores[unique] = 0

print('\nstarting ...')


d = dict()

for line in inf:
    line = line.strip().split("|")  # 0 -> letter, 1 -> suggestion , 2 -> answer
    d[line[0]] = {
        "suggestion": line[1],
        "answer": line[2]
    }
    
#print(d)

j = 0
for i in range(len(d)):
    print()
    player = players_list[j]
    letter = input('{}, please choose a letter: '.format(player)).upper()
    while True:
        if len(letter) == 1 and ('A' <= letter <= 'Z' or 'a' <= letter <= 'z'):
            try:
                description = d[letter]['suggestion']       
                break
            except KeyError:
                pass

        letter = input('not valid. Please rewrite: ').upper()

    j += 1
    if j == players:
        j = 0

    print('{} - {}'.format(letter, description))

    guess = input('enter your guess: ')
    guess = guess.upper().strip()
    actual_choice = d[letter]['answer']

    base64_bytes = actual_choice.encode('ascii')
    company_bytes = base64.b64decode(base64_bytes)
    company = company_bytes.decode('ascii')

    if guess == company:
        scores[player] += 1
        print('CORRECT!')
    else:
        print('wrong... it was {}'.format(company))

sorted_players = sorted(scores, key=scores.get, reverse=True)
winner_points = scores[sorted_players[0]] # return the winner player points

def find_winner(x):
    if scores[x] == winner_points:
        return True
    else:
        return False 
    
winners = list(filter(find_winner, sorted_players))

print()
if len(winners) == 1:
    print('the winner is {}'.format(winners[0]))
else:
    print('winners are {}'.format(', '.join(winners)))


    
