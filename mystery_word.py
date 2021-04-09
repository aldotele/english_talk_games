import os
import base64


# OPENING INPUT FILE
filename = input('enter txt file name: ')
inf = open(os.path.join('files', filename))

prize = int(input('enter starting prize: '))
print(f"€ {prize}")
print()

lines = inf.readlines()
last_lines = lines[-2:]
options = last_lines[0]
winning_word = last_lines[1]
if winning_word == '\n':
    print('please do not leave empty lines at the end of the txt file!')
    quit()

inf = open(os.path.join('files', filename))

count = 0
valid_hints = []

for line in inf:
    line = line.strip()
    if count < 5:
        split_line = line.split(' | ')
        print('1 - ', split_line[0])
        print('2 - ', split_line[1])
        answer = int(input('what is your choice? '))

        if str(answer - 1) != options[count]:
            prize = prize / 2
        # print(options[count])
        print(split_line[int(options[count])])
        valid_hints.append(split_line[int(options[count])])
        print(f"€ {prize}")
        print()

    count += 1

print()
for element in valid_hints:
    print(element)
print()
guess = input('what is the word? ')


winning_word_bytes = winning_word.encode('ascii')
decoded_bytes = base64.b64decode(winning_word_bytes)
winning_word = decoded_bytes.decode('ascii')

if guess.upper().strip() == winning_word:
    print(f'YOU WON € {prize}')
    print(f"the word is {winning_word}")
else:
    print('YOU LOST')
    print(f"the word is {winning_word}")
