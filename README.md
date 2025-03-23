# Pokémon TCG Game

A command-line implementation of the Pokémon Trading Card Game featuring rock-type Pokémon. This project simulates the core mechanics of the Pokémon TCG in a text-based interface with ASCII art visualization.

## Features

- Play against a computer opponent with strategic AI
- Deck of rock-type Pokémon (Geodude, Onix, Tyranitar, etc.)
- Energy and Trainer cards
- ASCII art display for cards and game board
- Prize card system
- Bench Pokémon
- Energy attachment mechanics
- Mulligan handling

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

- **pokemon_tcg.py**: Main game file containing game loop and turn logic
- **player.py**: Player class implementation with deck, hand, and gameplay methods
- **pokemon_cards.py**: Card definitions (Pokémon, Energy, and Trainer cards)
- **ascii_art.py**: ASCII art utilities for visualizing the game

## Requirements

- Python 3.6 or higher

## Project Overview

The game implements a simplified version of the Pokémon Trading Card Game with a focus on rock-type Pokémon. It follows these core mechanics:

- **Card Types**: Pokémon, Energy, and Trainer cards
- **Evolution**: Basic Pokémon can evolve into more powerful forms
- **Energy System**: Pokémon need energy cards to use attacks
- **Prize Cards**: Take prize cards when you knock out opponent's Pokémon
- **Active and Bench**: One active Pokémon in battle, up to 5 on bench

The implementation uses ASCII art to visualize the game state, making it playable in any terminal.

## License

This is a fan project and is not affiliated with or endorsed by Nintendo, The Pokémon Company, or Game Freak.

Enjoy the game! 