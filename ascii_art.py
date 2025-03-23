"""
ASCII Art Utilities for Pokémon TCG Game
"""

# ASCII art for each Pokémon
POKEMON_ASCII = {
    "Geodude": """
      _____
     /     \\
    |  O O  |
    |   v   |
    |  \\=/ _|
     \\_____/
    """,
    
    "Graveler": """
       _____
      /     \\
     |  o o  |
     | _\_/_ |
    /|       |\\
   / |       | \\
  /__|_______|__\\
    """,
    
    "Golem": """
      _______
     /       \\
    |  O   O  |
    |    v    |
    |_/\\_/\\_/\\_|
    (_)     (_)
    """,
    
    "Onix": """
           __
     _____/  \\
    /         \\
   /   O    O  \\
  |       v     |
  |   _______   |
   \\_/       \\_/
    """,
    
    "Rhyhorn": """
      /\\    /\\
     /  \\__/  \\
    |  O    O  |
    \\    /\\    /
     \\__/  \\__/
       |    |
    """,
    
    "Rhydon": """
     _  _
    / \\/ \\
   |o    o|
   |  \\/  |
   |      |
  /|______|\\
 / |      | \\
    """,
    
    "Sudowoodo": """
       Y
      YoY
     Y o Y
      /|\\
     / | \\
       |
      / \\
    """,
    
    "Larvitar": """
      /\\
     /  \\
    | oo |
    | -- |
    |    |
    |____|
    """,
    
    "Pupitar": """
    .---------.
    |  _   _  |
    | | | | | |
    | |_| |_| |
    |         |
    \\_________/
    """,
    
    "Tyranitar": """
     /\\_____/\\
    |  O   O  |
    |    v    |
    |_________|
      |     |
      |     |
      |_____|
    """
}

def print_title():
    """Print the game title in ASCII art"""
    print("""
 _____      _                              _______ _____ _____  
|  __ \\    | |                            |__   __/ ____|  __ \\ 
| |__) |__ | | _____ _ __ ___   ___  _ __    | | | |    | |  | |
|  ___/ _ \\| |/ / _ \\ '_ ` _ \\ / _ \\| '_ \\   | | | |    | |__| |
| |  | (_) |   <  __/ | | | | | (_) | | | |  | | | |____| |_| | 
|_|   \\___/|_|\\_\\___|_| |_| |_|\\___/|_| |_|  |_|  \\_____|____/ 
                                                               
    """)

def print_card(card, active=False):
    """Print a card in ASCII art"""
    width = 30
    if active:
        print("*" * (width + 4))
        print("* " + " " * width + " *")
    else:
        print("-" * (width + 4))
        print("| " + " " * width + " |")
    
    if card.card_type == "pokemon":
        if active:
            print(f"* {card.name.center(width)} *")
            
            # Add ASCII art for active Pokémon
            if card.name in POKEMON_ASCII:
                art_lines = POKEMON_ASCII[card.name].strip('\n').split('\n')
                for line in art_lines:
                    padded_line = line.center(width)
                    print(f"* {padded_line} *")
            
            print(f"* {'HP: ' + str(card.hp):<{width}} *")
            print(f"* {'Attack: ' + card.description:<{width}} *")
            print(f"* {'Damage: ' + str(card.damage):<{width}} *")
            print(f"* {'Energy: ' + str(card.attached_energy) + '/' + str(card.energy_cost):<{width}} *")
            print("* " + " " * width + " *")
            print("*" * (width + 4))
        else:
            print(f"| {card.name.center(width)} |")
            print(f"| {'HP: ' + str(card.hp):<{width}} |")
            print(f"| {'Attack: ' + card.description:<{width}} |")
            print(f"| {'Damage: ' + str(card.damage):<{width}} |")
            print(f"| {'Energy: ' + str(card.attached_energy) + '/' + str(card.energy_cost):<{width}} |")
            print("| " + " " * width + " |")
            print("-" * (width + 4))
    elif card.card_type == "energy":
        if active:
            print(f"* {card.name.center(width)} *")
            print(f"* {'ENERGY CARD'.center(width)} *")
            print(f"* {card.description.center(width)} *")
            print("* " + " " * width + " *")
            print("*" * (width + 4))
        else:
            print(f"| {card.name.center(width)} |")
            print(f"| {'ENERGY CARD'.center(width)} |")
            print(f"| {card.description.center(width)} |")
            print("| " + " " * width + " |")
            print("-" * (width + 4))
    else:  # Trainer
        if active:
            print(f"* {card.name.center(width)} *")
            print(f"* {'TRAINER CARD'.center(width)} *")
            print(f"* {card.description.center(width)} *")
            print("* " + " " * width + " *")
            print("*" * (width + 4))
        else:
            print(f"| {card.name.center(width)} |")
            print(f"| {'TRAINER CARD'.center(width)} |")
            print(f"| {card.description.center(width)} |")
            print("| " + " " * width + " |")
            print("-" * (width + 4))

def print_hand(hand):
    """Print the player's hand in a more detailed way"""
    print("\nYOUR HAND:")
    print("=" * 80)
    
    for i, card in enumerate(hand):
        print(f"{i+1}. {card}")
        if card.card_type == "pokemon" and card.name in POKEMON_ASCII:
            art_lines = POKEMON_ASCII[card.name].strip('\n').split('\n')
            for line in art_lines:
                print(f"   {line}")
        print("-" * 40)
    
    print("=" * 80)

def print_board(player, computer, show_computer_hand=False):
    """Print the current game board"""
    print("\n" + "=" * 80)
    print("COMPUTER".center(80))
    print(f"Deck: {len(computer.deck)} cards | Discard: {len(computer.discard)} cards")
    
    print("\nCOMPUTER'S ACTIVE POKEMON:")
    if computer.active_pokemon:
        print_card(computer.active_pokemon, active=True)
    else:
        print("No active Pokémon")
    
    print("\nCOMPUTER'S BENCH:")
    if computer.bench:
        for pokemon in computer.bench:
            print_card(pokemon)
    else:
        print("No Pokémon on bench")
    
    if show_computer_hand:
        print("\nCOMPUTER'S HAND:")
        for card in computer.hand:
            print(f"- {card}")
    else:
        print(f"\nCOMPUTER'S HAND: {len(computer.hand)} cards")
    
    print("\n" + "-" * 80 + "\n")
    
    print("PLAYER".center(80))
    print(f"Deck: {len(player.deck)} cards | Discard: {len(player.discard)} cards")
    
    print("\nYOUR ACTIVE POKEMON:")
    if player.active_pokemon:
        print_card(player.active_pokemon, active=True)
    else:
        print("No active Pokémon")
    
    print("\nYOUR BENCH:")
    if player.bench:
        for pokemon in player.bench:
            print_card(pokemon)
    else:
        print("No Pokémon on bench")
    
    print("\nYOUR HAND:")
    for i, card in enumerate(player.hand):
        print(f"{i+1}. {card}")
    
    print("=" * 80 + "\n")

def print_turn_banner(player_name):
    """Print a banner for whose turn it is"""
    banner = f"===== {player_name}'S TURN ====="
    print("\n" + "=" * len(banner))
    print(banner)
    print("=" * len(banner) + "\n")

def print_action(action_text):
    """Print an action with formatting"""
    print(f">> {action_text}")

def print_winner(winner):
    """Print the winner announcement"""
    print("\n" + "*" * 60)
    print(f"***** {winner} WINS THE GAME! *****".center(60))
    print("*" * 60 + "\n")

def print_help():
    """Print help information"""
    print("\n=== COMMANDS ===")
    print("1-N       - Play card from hand (number corresponds to card position)")
    print("attack    - Attack with your active Pokémon")
    print("end       - End your turn")
    print("help      - Show this help information")
    print("quit      - Quit the game")
    print("==============\n") 