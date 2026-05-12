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

# Enumerations
cards_Suit: Enumeration = Enumeration(
    name="cards_Suit",
    literals={
            
    }
)

# Classes
cards_Card = Class(name="cards_Card")
cards_PokerHand = Class(name="cards_PokerHand")
cards_Deck = Class(name="cards_Deck")
cards_CardsGUI = Class(name="cards_CardsGUI")
cards_PokerHandInterface_Interface = Class(name="cards_PokerHandInterface_Interface")
players_Player = Class(name="players_Player")
players_PlayerVersionGUI = Class(name="players_PlayerVersionGUI")
players_Person = Class(name="players_Person")
game_Ranker = Class(name="game_Ranker")
game_GameBoardGUI = Class(name="game_GameBoardGUI")
main_Play = Class(name="main_Play")

# cards_Card class attributes and methods
cards_Card_rank: Property = Property(name="rank", type=IntegerType)
cards_Card_suit: Property = Property(name="suit", type=cards_Suit)
cards_Card.attributes={cards_Card_suit, cards_Card_rank}

# cards_PokerHand class attributes and methods
cards_PokerHand_hand: Property = Property(name="hand", type=StringType)
cards_PokerHand_rank: Property = Property(name="rank", type=IntegerType)
cards_PokerHand.attributes={cards_PokerHand_rank, cards_PokerHand_hand}

# cards_Deck class attributes and methods
cards_Deck_cards: Property = Property(name="cards", type=StringType)
cards_Deck_remain: Property = Property(name="remain", type=IntegerType)
cards_Deck.attributes={cards_Deck_remain, cards_Deck_cards}

# cards_CardsGUI class attributes and methods

# cards_PokerHandInterface_Interface class attributes and methods

# players_Player class attributes and methods
players_Player_hand: Property = Property(name="hand", type=cards_PokerHand)
players_Player_hasFolded: Property = Property(name="hasFolded", type=BooleanType)
players_Player_curentChips: Property = Property(name="curentChips", type=IntegerType)
players_Player.attributes={players_Player_hand, players_Player_curentChips, players_Player_hasFolded}

# players_PlayerVersionGUI class attributes and methods

# players_Person class attributes and methods
players_Person_name: Property = Property(name="name", type=StringType)
players_Person_accountNumber: Property = Property(name="accountNumber", type=StringType)
players_Person.attributes={players_Person_accountNumber, players_Person_name}

# game_Ranker class attributes and methods
game_Ranker_hand: Property = Property(name="hand", type=cards_PokerHand)
game_Ranker_highValue: Property = Property(name="highValue", type=IntegerType)
game_Ranker.attributes={game_Ranker_highValue, game_Ranker_hand}

# game_GameBoardGUI class attributes and methods

# main_Play class attributes and methods
main_Play_players: Property = Property(name="players", type=StringType)
main_Play_plv: Property = Property(name="plv", type=players_PlayerVersionGUI)
main_Play_gb: Property = Property(name="gb", type=game_GameBoardGUI)
main_Play_cd: Property = Property(name="cd", type=cards_CardsGUI)
main_Play.attributes={main_Play_players, main_Play_cd, main_Play_gb, main_Play_plv}

# Domain Model
domain_model = DomainModel(
    name="__eT4YAw2EeihOuC11hdjgA",
    types={cards_Card, cards_PokerHand, cards_Deck, cards_CardsGUI, cards_PokerHandInterface_Interface, players_Player, players_PlayerVersionGUI, players_Person, game_Ranker, game_GameBoardGUI, main_Play, cards_Suit},
    associations={},
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