import random

WORDS = ["python", "terminal", "programming", "function", "variable", "keyboard"]
MAX_MISTAKES = 6

HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
    =======
    """,
]


def display_game(secret_word, guessed_letters, mistakes):
    """Show the gallows, the word progress, and the guessed letters."""
    print(HANGMAN_STAGES[mistakes])
    print("Word: " + " ".join(letter if letter in guessed_letters else "_" for letter in secret_word))
    print("Guessed letters: " + (" ".join(sorted(guessed_letters)) or "None"))
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}\n")


def play():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Hangman! Guess the hidden word one letter at a time.\n")

    while mistakes < MAX_MISTAKES:
        display_game(secret_word, guessed_letters, mistakes)

        if all(letter in guessed_letters for letter in secret_word):
            print(f"You won! The word was {secret_word!r}.")
            return

        guess = input("Enter one letter (or type 'quit' to exit): ").strip().lower()

        if guess == "quit":
            print(f"Game ended. The word was {secret_word!r}.")
            return
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.add(guess)
        if guess not in secret_word:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.\n")
        else:
            print(f"Good guess! '{guess}' is in the word.\n")

    display_game(secret_word, guessed_letters, mistakes)
    print(f"Game over! The word was {secret_word!r}.")


if __name__ == "__main__":
    play()
