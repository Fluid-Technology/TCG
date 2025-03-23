#!/usr/bin/env python3
"""
Pokémon TCG Game
A simple implementation of the Pokémon Trading Card Game with rock-type Pokémon.
"""

import time
import sys
from player import Player
from ascii_art import (
    print_title, print_board, print_turn_banner, 
    print_action, print_winner, print_help, print_hand
)

def clear_screen():
    """Clear the terminal screen"""
    print("\033[H\033[J", end="")

def slow_print(text, delay=0.03):
    """Print text with a slight delay for better readability"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def setup_game():
    """Initialize the game and players"""
    clear_screen()
    print_title()
    
    # Create players
    player = Player("PLAYER", is_computer=False)
    computer = Player("COMPUTER", is_computer=True)
    
    # Draw starting hands
    player.draw_starting_hand()
    computer.draw_starting_hand()
    
    # Handle mulligans
    player_mulligan = player.has_basic_pokemon()
    computer_mulligan = computer.has_basic_pokemon()
    
    while not player_mulligan:
        slow_print("You have no basic Pokémon! Performing a mulligan...")
        player_mulligan = not player.mulligan()
    
    while not computer_mulligan:
        slow_print("Computer has no basic Pokémon! Performing a mulligan...")
        computer_mulligan = not computer.mulligan()
    
    # Set up prize cards
    player.setup_prizes()
    computer.setup_prizes()
    
    return player, computer

def select_active_pokemon(player):
    """Let the player select their starting active Pokémon"""
    while True:
        print("\nSelect a basic Pokémon to be your active Pokémon:")
        basic_indices = []
        for i, card in enumerate(player.hand):
            if card.card_type == "pokemon" and card.energy_cost <= 1:
                basic_indices.append(i)
                print(f"{i+1}. {card}")
        
        try:
            choice = int(input("\nEnter card number: ")) - 1
            if choice in basic_indices:
                success, message = player.play_pokemon(choice, as_active=True)
                if success:
                    print_action(message)
                    return
            else:
                print("Invalid choice. Please select a basic Pokémon.")
        except ValueError:
            print("Please enter a number.")

def select_bench_pokemon(player):
    """Let the player select Pokémon for their bench"""
    while True:
        print("\nDo you want to place any basic Pokémon on your bench? (y/n)")
        choice = input().lower()
        
        if choice == 'n':
            return
        
        if choice == 'y':
            print("\nSelect a basic Pokémon for your bench:")
            basic_indices = []
            for i, card in enumerate(player.hand):
                if card.card_type == "pokemon" and card.energy_cost <= 1:
                    basic_indices.append(i)
                    print(f"{i+1}. {card}")
            
            if not basic_indices:
                print("No more basic Pokémon in your hand.")
                return
            
            try:
                card_choice = int(input("\nEnter card number (0 to stop): ")) - 1
                if card_choice == -1:
                    return
                
                if card_choice in basic_indices:
                    success, message = player.play_pokemon(card_choice, as_active=False)
                    if success:
                        print_action(message)
                    else:
                        print(message)
                else:
                    print("Invalid choice. Please select a basic Pokémon.")
            except ValueError:
                print("Please enter a number.")

def computer_setup(computer):
    """Set up the computer's active Pokémon and bench"""
    # Find all basic Pokémon in hand
    basic_indices = [i for i, card in enumerate(computer.hand) 
                   if card.card_type == "pokemon" and card.energy_cost <= 1]
    
    if not basic_indices:
        return  # Shouldn't happen due to mulligan checks
    
    # Play first as active
    success, message = computer.play_pokemon(basic_indices[0], as_active=True)
    if success:
        print_action(f"Computer {message.lower()}")
    
    # Play rest on bench (up to 5)
    basic_indices = basic_indices[1:]  # Remove the one we just played
    bench_count = 0
    
    for idx in basic_indices[:5]:  # Max 5 on bench
        # Adjust index because we're removing cards
        adjusted_idx = idx - bench_count
        success, message = computer.play_pokemon(adjusted_idx, as_active=False)
        if success:
            print_action(f"Computer {message.lower()}")
            bench_count += 1

def player_turn(player, computer):
    """Handle the player's turn"""
    print_turn_banner("PLAYER")
    
    # Start turn (draw a card)
    card = player.draw_card()
    if card is None:
        return "computer"  # Player loses if can't draw a card
    
    slow_print(f"You drew: {card}")
    player.can_attack = True
    
    # Display the player's hand with ASCII art
    print_hand(player.hand)
    
    while True:
        # Print the current game state
        print_board(player, computer)
        
        # Ask for action
        command = input("\nEnter command (help for list of commands): ").lower()
        
        if command == "help":
            print_help()
        
        elif command == "end":
            return "continue"  # End turn, game continues
        
        elif command == "quit":
            return "quit"  # Quit the game
        
        elif command == "attack":
            if not player.active_pokemon:
                print_action("You don't have an active Pokémon to attack with!")
                continue
                
            if not player.can_attack:
                print_action("You've already attacked this turn!")
                continue
                
            success, message = player.attack(computer)
            if success:
                print_action(message)
                
                # Check if computer's active was knocked out
                if not computer.active_pokemon and computer.bench:
                    # Computer must promote a new active
                    success, message = computer.choose_new_active()
                    if success:
                        print_action(f"Computer {message.lower()}")
                
                # Check win condition
                if not player.prizes:
                    return "player"  # Player wins by taking all prize cards
                
                if not computer.active_pokemon and not computer.bench:
                    return "player"  # Player wins by knocking out all Pokémon
            else:
                print_action(message)
        
        elif command.isdigit():
            # Play a card from hand
            card_index = int(command) - 1
            
            if card_index < 0 or card_index >= len(player.hand):
                print_action("Invalid card number!")
                continue
            
            card = player.hand[card_index]
            
            if card.card_type == "pokemon":
                # Determine if active or bench
                target = "active" if not player.active_pokemon else "bench"
                if target == "active":
                    success, message = player.play_pokemon(card_index, as_active=True)
                else:
                    if len(player.bench) >= 5:
                        print_action("Your bench is full! Cannot play more Pokémon.")
                        continue
                    success, message = player.play_pokemon(card_index, as_active=False)
                
                if success:
                    print_action(message)
                else:
                    print_action(message)
            
            elif card.card_type == "energy":
                # Choose target for energy
                if not player.active_pokemon and not player.bench:
                    print_action("You have no Pokémon to attach energy to!")
                    continue
                
                targets = []
                if player.active_pokemon:
                    targets.append(("active", player.active_pokemon))
                
                for i, pokemon in enumerate(player.bench):
                    targets.append((f"bench {i+1}", pokemon))
                
                print("\nChoose a Pokémon to attach energy to:")
                for i, (label, pokemon) in enumerate(targets):
                    print(f"{i+1}. {pokemon.name} ({label})")
                
                try:
                    target_choice = int(input("Enter choice number: ")) - 1
                    if 0 <= target_choice < len(targets):
                        target_type, _ = targets[target_choice]
                        if target_type == "active":
                            success, message = player.play_energy(card_index)
                        else:
                            bench_idx = int(target_type.split()[1]) - 1
                            success, message = player.play_energy(card_index, target_index=bench_idx)
                        
                        if success:
                            print_action(message)
                        else:
                            print_action(message)
                    else:
                        print_action("Invalid choice!")
                except ValueError:
                    print_action("Please enter a number.")
            
            elif card.card_type == "trainer":
                success, message = player.play_trainer(card_index)
                if success:
                    print_action(message)
                else:
                    print_action(message)
        
        else:
            print_action("Unknown command. Type 'help' for a list of commands.")
            
def computer_turn(computer, player):
    """Handle the computer's turn"""
    print_turn_banner("COMPUTER")
    
    # Start turn (draw a card)
    card = computer.draw_card()
    if card is None:
        return "player"  # Computer loses if can't draw a card
    
    slow_print(f"Computer drew a card.")
    computer.can_attack = True
    
    # Computer AI makes moves
    actions = computer.make_computer_move(player)
    
    # Display each action with a delay
    for action in actions:
        time.sleep(1)  # Slight delay between actions
        print_action(action)
    
    # Check if player's active was knocked out
    if not player.active_pokemon and player.bench:
        # Player must promote a new active
        success, message = player.choose_new_active()
        if success:
            print_action(message)
    
    # Check win conditions
    if not computer.prizes:
        return "computer"  # Computer wins by taking all prize cards
    
    if not player.active_pokemon and not player.bench:
        return "computer"  # Computer wins by knocking out all Pokémon
    
    # Print final board state after computer's turn
    print_board(player, computer)
    
    # Wait for player to acknowledge
    input("\nPress Enter to continue to your turn...")
    return "continue"

def main():
    """Main game loop"""
    player, computer = setup_game()
    
    # Initial setup phase
    slow_print("Setting up the game...")
    time.sleep(1)
    
    # Player chooses active Pokémon
    select_active_pokemon(player)
    
    # Player chooses bench Pokémon
    select_bench_pokemon(player)
    
    # Computer sets up
    slow_print("\nComputer is setting up...")
    computer_setup(computer)
    
    # Initial board state
    print_board(player, computer)
    input("\nPress Enter to start the game...")
    
    # Main game loop
    current_player = "player"  # Player goes first
    game_result = "continue"
    
    while game_result == "continue":
        if current_player == "player":
            game_result = player_turn(player, computer)
            current_player = "computer"
        else:
            game_result = computer_turn(computer, player)
            current_player = "player"
    
    # Game over
    if game_result == "player":
        print_winner("PLAYER")
    elif game_result == "computer":
        print_winner("COMPUTER")
    elif game_result == "quit":
        print("\nGame ended by player. Thanks for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0) 