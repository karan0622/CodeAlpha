import random
words = ["python", "apple", "banana", "computer", "coding"]

secret_word = random.choice(words)
display = ["_"] * len(secret_word)

incorrect_guesses = 0
max_attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print("You have 6 incorrect guesses.\n")


while incorrect_guesses < max_attempts and "_" in display:

    print("Word:", " ".join(display))
    print("Guessed letters:", guessed_letters)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

    else:
        incorrect_guesses += 1
        print(f"Wrong! Attempts left: {max_attempts - incorrect_guesses}")

    print()

if "_" not in display:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over!")
    print("The word was:", secret_word)  
