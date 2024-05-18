####################
#############ART####
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
################################################
#########################Word List##############
import wordlist 
################################################
#Choose a word from the word_list and assign to variable chosen_word
import random
chosen_word = random.choice(wordlist.word_list)
display = []
for _ in chosen_word:
    display += "_"
################################################
#needed variables
num_guess = len(chosen_word)
end_of_game = False
lives = 6
already_guessed = []
#############Main loop with user guess assigned to varialbe
while not end_of_game:
    guess = input("Guess a letter!:\n").lower()
################################################
#Check for and display guess if in chosen_word
    n = 0
    right_wrong = 0
    if guess in already_guessed:
        print("You have already guessed this letter!")
    for letter in chosen_word:
        if letter == guess:
            display[n] = guess
            n += 1
            right_wrong = 1
            already_guessed.append(guess)   
        else:
            n += 1
            already_guessed.append(guess)  
    print(f"{' '.join(display)}")
    if right_wrong == 1:
        print("Correct!")
        print(stages[lives])
    else:
        print(f"You guessed {guess}, thats not in the word. You lose a life!")
        lives = lives - 1
        print(stages[lives])
###########Has the player won or lost?    
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You lose!")
################################################
