# Hangman
import random
import hangman_art
import hangman_words

word = random.choice(hangman_words.word_list)
guess_word = []
end_of_game = False
lives = 6

print(hangman_art.logo + "\n")

# output word for easy testing
print(word)

# guess word
print(' '.join(guess_word)) 

# set the list to _
for _ in word:
    guess_word.append('_')

# loop until guess word = chosen word
while(end_of_game == False):

    guess = input("Guess a letter: ").lower()
    # check if letter exist in word
    if guess in guess_word:
        print(f"You already guessed {guess}.")

    for idx in range(len(word)):
        letter = word[idx]
        if letter == guess:
            guess_word[idx] = letter
    
    # guess word
    print(' '.join(guess_word)) 

    # Check if letter not in word, decrease life
    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(hangman_art.stages[lives])
        # if there's no live left
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    # Check if there's no _ left
    if "_" not in guess_word:
        end_of_game = True
        print(f"You win! The word is {word}")
