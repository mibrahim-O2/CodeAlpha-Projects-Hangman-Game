import random

words = ["python", "apple", "table", "chair", "light"]
word = random.choice(words)

guessed_word = ["_"] * len(word)

wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses allowed.\n")

while wrong_guesses < max_wrong and "_" in guessed_word:

    print("Word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!\n")
    else:
        wrong_guesses += 1
        print("Wrong! Remaining guesses:", max_wrong - wrong_guesses, "\n")

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
