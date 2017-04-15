
# Constraint one: Code without a computer.

It may sound silly, but I think this is the best thing to do to get better a programming.

There are many ways to structure code, and if you just dive in that inertia may block you from choosing better designs, or not wanting to refactor everything. It is not just the code today that we are thinking about it is the code tomorrow, when we have to come back to the code to update.

I spend a long time thinking about how to solve a problem vs actually coding the solution. Sometimes a day or more depending on the size. If it is updating legacy code, I may familiarize myself with code, and then walk away until I know how I want to update it.

If you don't have a solid idea of what you are doing you are going to do when you sit down, then you are probably going to waste time.

The one exception is with something completely unknown. Some new api, technology, or system call. Then you can explore, and work on a prototype. The goal of this is not to build a full piece of software or the full functionality, but just figure out how to manipulate this new thing. Then step back and figure out how to fit it in to the larger thing you are doing.

## Project One Part 1

Hangman. We are going to start with a very basic version of hangman.


```python
import random

words = ["Super","Awesome","Random"]

#random.choice(words)
#raw_input

```

* The program randomly picks a word to use out of words.

* It then shows the user a string of '_' characters, one per character of the hidden word.

* It prompts the user for a letter, if the letter is in word, it changes the '_' to that letter.

Keep in mind that the letter could be in the word multiple times.

*Repeat printing the current state of the word, and prompting the user until the word is guessed.

Example Run:

_ _ _ 

Enter letter:p 

P _ p 

Enter letter:i 

Word was: Pip 

Good Job

The goal of this exercise is to pseudo code, or even fully code this out, without using the computer. You can use pen and paper, or as you get better most of it can be held in your head.

What are you thinking about before you begin?


What data structures are you going to use? 

How will the code be broken up? Is all in main, are there multiple functions? 

Would be creating a new class or classes be useful?

Once you feel ready, code it up.

Notice how long it takes, notice how your ideas did or didn't work. Do you like the code?


## Part 2

Add the ability to display the hangman with the correct number of appendages based on the number incorrect. When the hangman is completely drawn the game is lost.

Example Run:
_ _ _ 
Enter letter:p
 O
_ _ _
Enter letter:z
 O
/
_ _ _
Enter letter:x
 O
/|

...

Until

 O
/|\
/ \

Draw from top to bottom, and left to right.

Think about how you will need to refactor the original code. Is there a lot to change? Maybe the original wasn't broken up that well.

Think about what happens when a product manager comes and says instead of left to right we want the body character '|' to be draw first on the second line.

You don't have to solve that now, but most software projects get revised, and getting better is understanding that you or someone will have to change the code.

You are not just building the code for now, but for future extensions.
