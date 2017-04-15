import sys
import random

words = ["Super","Awesome","Random"]
hangman = [' O\n','/','|','\\\n',' |\n','/ ','\\\n']


def draw_hangman(steps):
    map(lambda x: sys.stdout.write(x), hangman[0:steps])

def update_all_letters(hangman_line,word,user_letter):
    for index,letter in enumerate(word):
        if user_letter == letter:
            hangman_line[index] = letter
    
def play(word):
    hangman_line = ["_" for i in range(0,len(word))]
    incorrect_guesses = 0
    
    while incorrect_guesses < len(hangman) and '_' in hangman_line:
        print " ".join(hangman_line)

        draw_hangman(incorrect_guesses)
        
        user_letter = raw_input("\nEnter letter:").lower()

        if user_letter in word:
            update_all_letters(hangman_line,word,user_letter)
        else:
            incorrect_guesses += 1

    print "Word was: ",word

    
play(random.choice(words).lower())


