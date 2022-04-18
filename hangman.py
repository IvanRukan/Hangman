import random
import string

not_in_word = []
answers = ['python', 'kotlin', 'java', 'javascript']
print('H A N G M A N')
gg = ' '
while gg != 'play' or gg != 'exit':
    gg = input('Type "play" to play the game, "exit" to quit: ')
    if gg == 'play':
        answer = random.choice(answers)
        tries = 8
        begin = '-'
        stroka = ''
        stroka = begin * len(answer)
        while tries != 0:
            print()
            print(stroka)
            us_input = input('Input a letter: ')
            if len(us_input) != 1:
                print('You should input a single letter')
                continue
            if us_input not in string.ascii_lowercase:
                print('Please enter a lowercase English letter')
                continue

            if us_input in answer and us_input not in stroka:
                if answer.count(us_input) > 1:
                    let1 = answer.find(us_input)
                    let2 = answer.rfind(us_input)
                    stroka = list(stroka)
                    stroka[let1] = us_input
                    stroka[let2] = us_input
                    stroka =''.join(stroka)
                    if stroka == answer:
                        print(stroka)
                        print('You guessed the word!')
                        print('You survived!')
                        break


                elif answer.count(us_input) == 1:
                    let1 = answer.find(us_input)
                    stroka = list(stroka)
                    stroka[let1] = us_input
                    stroka =''.join(stroka)
                    if stroka == answer:
                        print(stroka)
                        print('You guessed the word!')
                        print('You survived!')
                        break
            elif us_input in stroka or us_input in not_in_word:
                print("You've already guessed this letter")

            else:
                print("That letter doesn't appear in the word")
                not_in_word.append(us_input)
                tries -= 1
        if stroka != answer:
            print('You lost!')
        break
    elif gg == 'exit':
        break
    else:
        continue
