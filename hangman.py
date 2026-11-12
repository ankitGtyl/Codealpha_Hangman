import random


words = ["Codealpha", "linkdin", "coding", "student", "laptop"]
# Convert to lowercase so case-sensitive comparisons don't fail
random_word = random.choice(words).lower()

guessed_letters = []
max_attempts = 6
incorrect_guesses = 0

print("="*10,"Welcome to Hangman!", "="*10)
print("You have 6 attempts to guess the correct word.\n")

while incorrect_guesses < max_attempts:
    display_word = ""
    for letter in random_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Word:", display_word.strip())
    print(f"Incorrect attempts remaining: {max_attempts - incorrect_guesses}")
    print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    

    guess = input("Guess a letter: ").lower().strip()
    print()  

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.\n")
        continue

    
    guessed_letters.append(guess)

    
    if guess in random_word:
        print(f"Good job! '{guess}' is in the word.\n")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! '{guess}' is not in the word.\n")

    
    won = True
    for letter in random_word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        print("🎉 Congratulations! You guessed the word correctly:", random_word)
        break

if incorrect_guesses == max_attempts:
    print("Game Over! You've used all your attempts.")
    print("The secret word was:", random_word)

