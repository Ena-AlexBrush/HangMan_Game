import random
from random_words import words_list
import art
import turtle

place_holder = ""
lives = 6
correctLetters = []
random_word = words_list[random.randint(0,len(words_list) - 1)] #or random.choice(words_list)
print(random_word)
game_over = False

#Replacing the word with underscore
for letters in random_word:
    place_holder += "_"

print("Welcome to Hangman! For every wrong answer, you lose one live!")
print(art.drawings[6])
print(place_holder)

while not game_over:
    user_guess = str(input("Guess a letter!: \n").lower())
    display = ""
    if(user_guess in correctLetters):
        print("You have already used this letter!")

    for letter in random_word:
        if(letter == user_guess):
            display += letter
            correctLetters.append(letter)
        elif(letter in correctLetters):
            display += letter
        else:
            display += "_"
    print(display)

    if(user_guess not in random_word):
        lives -= 1
        print("You guessed the wrong letter! \n")
        print(art.drawings[lives])
        print(f"You have these many lives: {lives}")
        print(display)
        if(lives == 0):
            game_over = True
            print(f"You lose :(\nThe word is {random_word}")


    if("_" not in display):
        game_over = True;
        print("You win")
