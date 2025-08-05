import random

def hangman():
    words = ['JAVASCRIPT', 'PYTHON', 'DEVELOPER', 'COMPUTER', 'HANGMAN', 'MAHIMA','AYUSH','RIYA','BHARTI']
    selected_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time. You have 6 incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in selected_word])
        print(f"\nCurrent word: {display_word}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Get user input
        guess = input("Enter a letter: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        if guess in selected_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check if the word has been completely guessed
        if all(letter in guessed_letters for letter in selected_word):
            print(f"Congratulations! You guessed the word: {selected_word}")
            break
    else:
        print(f"Game over! The word was: {selected_word}")

if __name__ == "__main__":
    hangman()

