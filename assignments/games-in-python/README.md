
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game that uses strings, loops, conditionals, random selection, and user input. Players will guess a hidden word before they run out of incorrect guesses.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Use the provided word list to randomly select a secret word, initialize the game state, and display the letters the player has guessed correctly so far.

#### Requirements
Completed program should:

- Randomly choose one word from the provided `words` list.
- Track guessed letters and the number of incorrect guesses, with a maximum of 6 incorrect guesses.
- Display each secret-word letter as a blank until it has been guessed, such as `_ _ _`.

### 🛠️ Run a Complete Game

#### Description
Create the game loop so the player can enter guesses, see the updated word and remaining attempts, and receive a clear result when the game ends.

#### Requirements
Completed program should:

- Ask the player to guess one letter on each turn and compare the guess without case sensitivity.
- Update the displayed word for correct guesses and decrease the remaining attempts for incorrect guesses.
- End when the player guesses every letter or has no incorrect guesses remaining.
- Display a win message when the word is guessed and a loss message that reveals the secret word when attempts run out.
