# Pokémon TCG Game

A simple command-line implementation of the Pokémon Trading Card Game with rock-type Pokémon.

## Features

- Play against a computer opponent
- Rock-type Pokémon deck
- ASCII art display for cards and game board
- Simple turn-based gameplay

## How to Play

1. Run the game:
   ```
   python pokemon_tcg.py
   ```

2. Game Setup:
   - You'll be dealt a hand of 7 cards
   - Choose a basic Pokémon as your active Pokémon
   - Optionally place basic Pokémon on your bench
   - The computer will also set up its side

3. Game Commands:
   - `1-9`: Play the card at that position from your hand
   - `attack`: Attack with your active Pokémon
   - `end`: End your turn
   - `help`: Show available commands
   - `quit`: Quit the game

4. Gameplay Rules:
   - Draw a card at the start of your turn
   - You can play one energy card per turn
   - You can play multiple Pokémon to your bench (up to 5)
   - To attack, your active Pokémon needs enough energy
   - You win by taking all 6 prize cards or defeating all of your opponent's Pokémon

## Game Structure

- `pokemon_tcg.py`: Main game file
- `pokemon_cards.py`: Card definitions
- `player.py`: Player class implementation
- `ascii_art.py`: ASCII art utilities

## Requirements

- Python 3.6 or higher

Enjoy the game! 