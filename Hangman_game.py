import random 
from random_word import RandomWords

print("Hangman Game")

r = RandomWords()
word = r.get_random_word()
wrong_guess = 0
max_chances = 6
guessed_letters = []
hangmaan_parts = [
    """
      +---+
          |
          |
          |
          |
          |
    =========""",
    """
      +---+
      O   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      O   |
      |   |
          |
          |
          |
    =========""",
    """
      +---+
      O   |
     /|   |
          |
          |
          |
    =========""",
    """
      +---+
      O   |
     /|\  |
          |
          |
          |
    =========""",
    """
      +---+
      O   |
     /|\  |
     /    |
          |
          |
    =========""",
    """
      +---+
      O   |
     /|\  |
     / \  |
          |
          |
    =========""",
]

display = len(word) * ['_'] 

print("You have 6 chances to guess the word")

while wrong_guess < max_chances and '_' in display:
    print(hangmaan_parts[wrong_guess])
    print(' '.join(display))
    guess = input("Guess the letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed {guess} Try again!")

    else:
        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print(f"Correct! {guess} is in word")

        else:
            wrong_guess += 1
            print(f"Wrong! {guess} is not in word. You have {max_chances-wrong_guess} chances left") 
                
print()

if '_' not in display:
    print(f"You guessed the word {word}")
else:
    print(f"You ran out of chances. The word was {word}")
    print(hangmaan_parts[wrong_guess])