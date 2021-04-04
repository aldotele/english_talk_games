import os


inf = open(os.path.join('files', 'mw1.txt'))

prize = 480000
print(prize, 'euro')
print()

lines = inf.readlines()
last_lines = lines[-2:]
options = last_lines[0]
winning_word = last_lines[1]
# print(options)

inf = open(os.path.join('files', 'mw1.txt'))

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
        print(prize, ' euro')
        print()

    count += 1

print()
for element in valid_hints:
    print(element)
print()
guess = input('what is the word?')
if guess.upper() == winning_word:
    print('YOU WON', prize)
    print(winning_word)
else:
    print('YOU LOST')
    print(winning_word)