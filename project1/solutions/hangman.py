import random

words = ["Super","Awesome","Random"]

def play(word):
    hangman_line = ["_" for i in range(0,len(word))]

    while '_' in hangman_line:
        print " ".join(hangman_line)

        user_letter = raw_input("Enter letter:").lower()
    
        for index,letter in enumerate(word):
            if user_letter == letter.lower():
                hangman_line[index] = letter

    print "Word was: ",word

play(random.choice(words))



    


