"""
Pokemon TCG Card Definitions
Contains all the card data for the game
"""

class Card:
    def __init__(self, name, card_type, hp=0, damage=0, energy_cost=0, description=""):
        self.name = name
        self.card_type = card_type  # "pokemon", "energy", "trainer"
        self.hp = hp
        self.damage = damage
        self.energy_cost = energy_cost
        self.description = description
        self.attached_energy = 0

    def __str__(self):
        if self.card_type == "pokemon":
            return f"{self.name} (HP: {self.hp}, DMG: {self.damage}, Energy: {self.attached_energy}/{self.energy_cost})"
        elif self.card_type == "energy":
            return f"{self.name} Energy"
        else:
            return f"{self.name} ({self.description})"

# Define Rock-type Pokémon
ROCK_POKEMON = [
    Card("Geodude", "pokemon", hp=60, damage=20, energy_cost=1, description="Rock Throw"),
    Card("Graveler", "pokemon", hp=90, damage=40, energy_cost=2, description="Rock Slide"),
    Card("Golem", "pokemon", hp=120, damage=70, energy_cost=3, description="Earthquake"),
    Card("Onix", "pokemon", hp=90, damage=30, energy_cost=2, description="Rock Throw"),
    Card("Rhyhorn", "pokemon", hp=80, damage=30, energy_cost=2, description="Horn Attack"),
    Card("Rhydon", "pokemon", hp=100, damage=50, energy_cost=3, description="Horn Drill"),
    Card("Sudowoodo", "pokemon", hp=70, damage=30, energy_cost=1, description="Rock Throw"),
    Card("Larvitar", "pokemon", hp=50, damage=10, energy_cost=1, description="Bite"),
    Card("Pupitar", "pokemon", hp=70, damage=30, energy_cost=2, description="Rock Slide"),
    Card("Tyranitar", "pokemon", hp=130, damage=80, energy_cost=4, description="Hyper Beam"),
]

# Define Energy cards
ENERGY_CARDS = [
    Card("Rock", "energy", description="Provides energy for Rock-type Pokémon"),
] * 20  # 20 energy cards

# Define Trainer cards
TRAINER_CARDS = [
    Card("Potion", "trainer", description="Heal 20 damage from one of your Pokémon"),
    Card("Energy Retrieval", "trainer", description="Add an energy card from your discard pile to your hand"),
    Card("Professor's Research", "trainer", description="Discard your hand and draw 7 cards"),
    Card("Switch", "trainer", description="Switch your active Pokémon with one on your bench"),
    Card("Pokémon Center", "trainer", description="Heal all damage from your active Pokémon"),
]

# Create default rock deck
def create_rock_deck():
    import random
    deck = ROCK_POKEMON.copy() + ENERGY_CARDS.copy() + TRAINER_CARDS.copy()
    random.shuffle(deck)
    return deck 