import os
import base64
import time


# asking input file
filename = input('enter txt file name: ')
try:
    inf = open(os.path.join('files', filename))
except FileNotFoundError:
    print('input file was not found. Please retry.')
    quit()

# asking starting prize
try:
    prize = int(input('enter starting prize: '))
except:
    print('prize is not valid. Please retry.')
    quit()

print(f"€ {prize}")
print()

# each line will become an element of a list
lines = inf.readlines()

# getting the useful information in order to make the program work
useful_lines = []
for el in lines:
    if el != '\n':  # ignoring empty lines
        useful_lines.append(el)

# input files always have 7 lines (5 for word options, 2 for winning info)
if len(useful_lines) != 7:
    print('error: input file not valid')
    quit()

winning_info = useful_lines[-2:]
# storing the sequence of binary for the 5 valid words from the 6th line of the file
options = winning_info[0]
winning_word = winning_info[1]

if winning_word == '\n':
    print('please do not leave empty lines at the end of the txt file!')
    quit()

inf = open(os.path.join('files', filename))

count = 0
valid_hints = []  # it will store the 5 correct words/hints to guess the final single word

for line in inf:
    line = line.strip()
    # in the first 5 lines, there will be a pair of words that will be shown to the user
    if count < 5:
        split_line = line.split(' | ')
        # first option (a word)
        print('1 - ', split_line[0])
        # second option (a word)
        print('2 - ', split_line[1])

        try:
            answer = int(input('what is your choice? '))
        except:
            answer = 0  # each answer different from 1 or 2 will be counted as zero (not valid answer)

        # if the chosen word is the wrong one, the prize get halved
        if str(answer - 1) != options[count]:  # subtracting 1 because the shown options are 1 and 2 (not 0 and 1)
            prize = prize / 2
        # print(options[count])
        print(split_line[int(options[count])])  # correct word is shown
        valid_hints.append(split_line[int(options[count])])
        print(f"€ {prize}")  # showing the updated prize
        print()

    count += 1

# showing the 5 correct words/hints
print()
for element in valid_hints:
    print(element)
print()

# 60 seconds Timer
print('You have 60 seconds to think...')
time.sleep(60)
# requesting the user to write its guess
guess = input('what is the word? ')

# decoding the winning word (in the input file, it is not clear but written as base64)
winning_word_bytes = winning_word.encode('ascii')
decoded_bytes = base64.b64decode(winning_word_bytes)
winning_word = decoded_bytes.decode('ascii')  # this will be the clear word

# checking if the user won
if guess.upper().strip() == winning_word:  # ignoring case and spaces
    print(f'YOU WON € {prize}')
    print(f"the word is {winning_word}")
else:
    print('YOU LOST')
    print(f"the word is {winning_word}")
