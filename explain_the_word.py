import random
import os

people = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5']

filename = input('enter the name of the file to use: ')
words = open(os.path.join('files', filename))
words = words.read().splitlines()

count_people = len(people)
word_per_people = len(words) // count_people

d = {}
random.shuffle(words)

starting_index = 0
for person in people:
    d[person] = words[starting_index:starting_index + word_per_people]
    starting_index += word_per_people

# print(d)

a = 0
while a < word_per_people:

    for person in people:
        print(f'{person} --> {d[person][a]}')
        input()

    a += 1
