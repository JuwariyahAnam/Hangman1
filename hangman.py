import random
words = ["python", "apple", "computer", "science", "hangman"]
secret_word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

while wrong_guesses < max_attempts:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", max_attempts - wrong_guesses)
    if all(letter in guessed_letters for letter in secret_word):
        print("You guessed the word! You win!")
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.add(guess)
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
if wrong_guesses == max_attempts:
    print("You lost! The word was:", secret_word)
