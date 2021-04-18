import random
import os


# choosing file to use
filename = input('enter the name of the file to use: ')
try:
    words = open(os.path.join('files', filename))
except FileNotFoundError:
    print('input file was not found. Please retry.')
    quit()

# registering players
players = []
while True:
    player = input('enter player: ')
    if player != '':
        players.append(player)
    else:
        break


words = words.read().splitlines()
count_players = len(players)
word_per_player = len(words) // count_players

d = {}
random.shuffle(words)

starting_index = 0
for player in players:
    d[player] = words[starting_index:starting_index + word_per_player]
    starting_index += word_per_player

print()
print('**GAME STARTED**')
print()
a = 0
while a < word_per_player:

    for player in players:
        print(f'{player} --> {d[player][a]}')
        input()

    a += 1
