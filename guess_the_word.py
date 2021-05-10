import os
import base64

# Input the file to use
while True:
    input_file = input('write the input file to use: ')
    try:
        inf = open(os.path.join('files', input_file))
        break
    except FileNotFoundError:
        print('[x]Error: file not found, please re', end='')

# Input the number of the players
players = -1
for attempt in range(1, 4):
    try:
        players = int(input("How many players? "))
        break
    except:
        print('[x]Error: invalid input, please retry (attempts: %d/3)' % attempt)
if players == -1:
    print('[x]ERROR: Too many attempts')
    quit()

# Initializing players scores and list.
players_list = []
scores = dict()

# Take in input the players name and make it unique
for p in range(players):
    player_name = input("Player's name: ")
    unique = f"{player_name}_{p}"
    players_list.append(unique)
    scores[unique] = 0

# Loading all the questions into a dictionary
print('\n[...] Starting the game')
d = dict()
for line in inf:
    line = line.strip().split("|")  # 0 -> letter, 1 -> suggestion , 2 -> answer
    d[line[0]] = {
        "suggestion": line[1],
        "answer": line[2]
    }

# Dividing the game into rounds
rounds = len(d) // players
for i in range(rounds):
    print('\n[!] Round %d/%d' % (i + 1, rounds))
    for player in players_list:

        # Make player choose the letter
        print('\tAvailable letters:', *[ letters for letters in d ])
        while True:
            letter = input('{}, please choose one: '.format(player)).upper()
            if len(letter) == 1 and 'A' <= letter <= 'Z':
                try:
                    description = d[letter]['suggestion']
                    break
                except KeyError:
                    pass
            print('[x]Error: invalid input. Please retry')

        # Input the guess of the user
        print('{} - {}'.format(letter, description))
        guess = input('enter your guess: ').strip().upper()

        # Decoding the real answer check if the guess is correct
        actual_choice = d[letter]['answer']
        base64_bytes = actual_choice.encode('ascii')
        company_bytes = base64.b64decode(base64_bytes)
        actual_choice = company_bytes.decode('ascii')
        if guess == actual_choice:
            scores[player] += 1
            print('[v] CORRECT!\n')
        else:
            print('wrong... it was {}\n'.format(actual_choice))
        del d[letter]

# Finding the winner/s
sorted_players = sorted(scores, key=scores.get, reverse=True)
winner_points = scores[sorted_players[0]] # return the winner player points
def find_winner(x):
    return scores[x] == winner_points
winners = list(filter(find_winner, sorted_players))

# Announcing the winner/s and display the complete leaderboard
if len(winners) == 1:
    print('\n\tThe winner is {}'.format(winners[0]))
else:
    print('\n\tThe winners are {}'.format(', '.join(winners)))
for player in scores:
    print(player, '\t-', scores[player])
