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
Card = Class(name="Card")
Deck = Class(name="Deck")
GameBoard = Class(name="GameBoard")
Player = Class(name="Player")
GUI = Class(name="GUI")

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card_suit: Property = Property(name="suit", type=IntegerType)
Card.attributes={Card_value, Card_suit}

# Deck class attributes and methods

# GameBoard class attributes and methods
GameBoard_garbagePile: Property = Property(name="garbagePile", type=StringType)
GameBoard_discardPile: Property = Property(name="discardPile", type=StringType)
GameBoard_shelf: Property = Property(name="shelf", type=StringType)
GameBoard.attributes={GameBoard_garbagePile, GameBoard_shelf, GameBoard_discardPile}

# Player class attributes and methods
Player_points: Property = Property(name="points", type=IntegerType)
Player_hand: Property = Property(name="hand", type=Deck)
Player.attributes={Player_points, Player_hand}

# GUI class attributes and methods

# Relationships
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
GameBoard_Deck: BinaryAssociation = BinaryAssociation(
    name="GameBoard_Deck",
    ends={
        Property(name="deck2", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="gameBoard3", type=GameBoard, multiplicity=Multiplicity(0, 1))
    }
)
Player_Deck: BinaryAssociation = BinaryAssociation(
    name="Player_Deck",
    ends={
        Property(name="deck4", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="player5", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
GameBoard_GUI: BinaryAssociation = BinaryAssociation(
    name="GameBoard_GUI",
    ends={
        Property(name="gUI6", type=GUI, multiplicity=Multiplicity(0, 1)),
        Property(name="gameBoard7", type=GameBoard, multiplicity=Multiplicity(0, 1))
    }
)
Player_GameBoard: BinaryAssociation = BinaryAssociation(
    name="Player_GameBoard",
    ends={
        Property(name="gameBoard8", type=GameBoard, multiplicity=Multiplicity(0, 1)),
        Property(name="player9", type=Player, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Wr1DEORqEemtQJ5uHCArog",
    types={Card, Deck, GameBoard, Player, GUI},
    associations={Deck_Card, GameBoard_Deck, Player_Deck, GameBoard_GUI, Player_GameBoard},
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