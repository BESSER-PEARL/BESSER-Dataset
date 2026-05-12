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
CardSuit: Enumeration = Enumeration(
    name="CardSuit",
    literals={
            
    }
)

CardTitle: Enumeration = Enumeration(
    name="CardTitle",
    literals={
            
    }
)

# Classes
Deck = Class(name="Deck")
Cards = Class(name="Cards")
Player = Class(name="Player")
Hand = Class(name="Hand")
Dealer = Class(name="Dealer")
HandValue = Class(name="HandValue")
Game = Class(name="Game")

# Deck class attributes and methods

# Cards class attributes and methods
Cards_value: Property = Property(name="value", type=IntegerType)
Cards_suit: Property = Property(name="suit", type=CardSuit)
Cards_title: Property = Property(name="title", type=CardTitle)
Cards.attributes={Cards_value, Cards_suit, Cards_title}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name}

# Hand class attributes and methods
Hand_value: Property = Property(name="value", type=HandValue)
Hand.attributes={Hand_value}

# Dealer class attributes and methods
Dealer_name: Property = Property(name="name", type=StringType)
Dealer_cards: Property = Property(name="cards", type=Cards)
Dealer.attributes={Dealer_name, Dealer_cards}

# HandValue class attributes and methods

# Game class attributes and methods
Game_winner: Property = Property(name="winner", type=Player)
Game.attributes={Game_winner}

# Relationships
Player_Game: BinaryAssociation = BinaryAssociation(
    name="Player_Game",
    ends={
        Property(name="game0", type=Game, multiplicity=Multiplicity(1, 1)),
        Property(name="player1", type=Player, multiplicity=Multiplicity(2, 9))
    }
)
Game_Dealer: BinaryAssociation = BinaryAssociation(
    name="Game_Dealer",
    ends={
        Property(name="dealer2", type=Dealer, multiplicity=Multiplicity(1, 1)),
        Property(name="game3", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Cards: BinaryAssociation = BinaryAssociation(
    name="Deck_Cards",
    ends={
        Property(name="cards4", type=Cards, multiplicity=Multiplicity(52, 52)),
        Property(name="deck5", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Hand_Player: BinaryAssociation = BinaryAssociation(
    name="Hand_Player",
    ends={
        Property(name="player6", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="hand7", type=Hand, multiplicity=Multiplicity(1, 1))
    }
)
HandValue_Hand: BinaryAssociation = BinaryAssociation(
    name="HandValue_Hand",
    ends={
        Property(name="hand8", type=Hand, multiplicity=Multiplicity(0, 1)),
        Property(name="handValue9", type=HandValue, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Deck: BinaryAssociation = BinaryAssociation(
    name="Dealer_Deck",
    ends={
        Property(name="deck10", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer11", type=Dealer, multiplicity=Multiplicity(1, 1))
    }
)
Hand_Cards: BinaryAssociation = BinaryAssociation(
    name="Hand_Cards",
    ends={
        Property(name="cards12", type=Cards, multiplicity=Multiplicity(5, 5)),
        Property(name="hand13", type=Hand, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_fV2LcAtNEeihOuC11hdjgA",
    types={Deck, Cards, Player, Hand, Dealer, HandValue, Game, CardSuit, CardTitle},
    associations={Player_Game, Game_Dealer, Deck_Cards, Hand_Player, HandValue_Hand, Dealer_Deck, Hand_Cards},
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