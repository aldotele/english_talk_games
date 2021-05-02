import os
import base64
 

players = int(input("How many players? "))
players_list = []

for p in range(players):
    player_name = input("Player's name: ")
    players_list.append(player_name)
print('\nstarting ...')

inf = open(os.path.join('files', 'sample.txt'))

d = dict()

for line in inf:
    line = line.strip().split("|") # 0 -> letter, 1 -> suggestion , 2 -> answer
    d[line[0]] = {
        "suggestion": line[1],
        "answer": line[2]
    }
    
#print(d)

j = 0
for i in range(len(d)):
    print()
    player = players_list[j]
    letter = input('{}, please choose a letter: '.format(player))
    while True:
        if len(letter) == 1 and ('A' <= letter <= 'Z' or 'a' <= letter <= 'z'):
            break
        letter = input('not valid. Please rewrite: ')

    letter = letter.upper()
    j += 1
    if j == players:
        j = 0

    print('{} - {}'.format(letter, d[letter]['suggestion']))
    guess = input('enter your guess: ')
    guess = guess.upper()
    actual_choice = d[letter]['answer']

    base64_bytes = actual_choice.encode('ascii')
    company_bytes = base64.b64decode(base64_bytes)
    company = company_bytes.decode('ascii')

    if guess == company:
        print('CORRECT!')
    else:
        print('wrong... the company is {}'.format(company))



    
