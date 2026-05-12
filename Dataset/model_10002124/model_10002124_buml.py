####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
BlackJackApp = Class(name="BlackJackApp")
BlackJack_Hra = Class(name="BlackJack_Hra")
Deck = Class(name="Deck")
Card = Class(name="Card")
Hand = Class(name="Hand")

# BlackJackApp class attributes and methods

# BlackJack_Hra class attributes and methods
BlackJack_Hra_bet: Property = Property(name="bet", type=StringType)
BlackJack_Hra_money: Property = Property(name="money", type=StringType)
BlackJack_Hra_deck: Property = Property(name="deck", type=StringType)
BlackJack_Hra_players_hand: Property = Property(name="players_hand", type=StringType)
BlackJack_Hra_dealers_hand: Property = Property(name="dealers_hand", type=StringType)
BlackJack_Hra_play: Property = Property(name="play", type=StringType)
BlackJack_Hra_placebet: Property = Property(name="placebet", type=StringType)
BlackJack_Hra_deal: Property = Property(name="deal", type=StringType)
BlackJack_Hra_player_wins: Property = Property(name="player_wins", type=StringType)
BlackJack_Hra_dealer_wins: Property = Property(name="dealer_wins", type=StringType)
BlackJack_Hra_tie: Property = Property(name="tie", type=StringType)
BlackJack_Hra_player_asks_for_card: Property = Property(name="player_asks_for_card", type=StringType)
BlackJack_Hra_show_result: Property = Property(name="show_result", type=StringType)
BlackJack_Hra.attributes={BlackJack_Hra_players_hand, BlackJack_Hra_tie, BlackJack_Hra_bet, BlackJack_Hra_play, BlackJack_Hra_player_asks_for_card, BlackJack_Hra_deal, BlackJack_Hra_show_result, BlackJack_Hra_money, BlackJack_Hra_placebet, BlackJack_Hra_dealer_wins, BlackJack_Hra_deck, BlackJack_Hra_dealers_hand, BlackJack_Hra_player_wins}

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=StringType)
Deck_top_card: Property = Property(name="top_card", type=StringType)
Deck_random: Property = Property(name="random", type=StringType)
Deck_deck: Property = Property(name="deck", type=StringType)
Deck_shuffle: Property = Property(name="shuffle", type=StringType)
Deck_random_cards: Property = Property(name="random_cards", type=StringType)
Deck_deal_card: Property = Property(name="deal_card", type=StringType)
Deck.attributes={Deck_deck, Deck_random, Deck_shuffle, Deck_cards, Deck_top_card, Deck_deal_card, Deck_random_cards}

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_cards: Property = Property(name="cards", type=StringType)
Card.attributes={Card_cards, Card_value, Card_suit}

# Hand class attributes and methods
Hand_num_card: Property = Property(name="num_card", type=IntegerType)
Hand_max_cards: Property = Property(name="max_cards", type=IntegerType)
Hand_hand: Property = Property(name="hand", type=StringType)
Hand_addcard: Property = Property(name="addcard", type=StringType)
Hand_blackjack: Property = Property(name="blackjack", type=BooleanType)
Hand_under: Property = Property(name="under", type=StringType)
Hand_bestscore: Property = Property(name="bestscore", type=StringType)
Hand_must_hit: Property = Property(name="must_hit", type=BooleanType)
Hand_busted: Property = Property(name="busted", type=StringType)
Hand.attributes={Hand_busted, Hand_under, Hand_num_card, Hand_addcard, Hand_bestscore, Hand_max_cards, Hand_must_hit, Hand_hand, Hand_blackjack}

# Relationships
BlackJackApp_BlackJack_Hra: BinaryAssociation = BinaryAssociation(
    name="BlackJackApp_BlackJack_Hra",
    ends={
        Property(name="blackJack_Hra0", type=BlackJack_Hra, multiplicity=Multiplicity(0, 1)),
        Property(name="blackJackApp1", type=BlackJackApp, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_q7xScNWnEeehRMl7r1_c5g",
    types={BlackJackApp, BlackJack_Hra, Deck, Card, Hand},
    associations={BlackJackApp_BlackJack_Hra},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)