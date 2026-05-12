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
Board: Enumeration = Enumeration(
    name="Board",
    literals={
            
    }
)

# Classes
Deck = Class(name="Deck")
Player = Class(name="Player")
ElevensGame = Class(name="ElevensGame")
Card_Interface = Class(name="Card_Interface")

# Deck class attributes and methods
Deck_Topcard: Property = Property(name="Topcard", type=IntegerType)
Deck_Deck_ArrayList_: Property = Property(name="Deck_ArrayList_", type=IntegerType)
Deck.attributes={Deck_Topcard, Deck_Deck_ArrayList_}

# Player class attributes and methods

# ElevensGame class attributes and methods
ElevensGame_win: Property = Property(name="win", type=BooleanType)
ElevensGame_Board_9_: Property = Property(name="Board_9_", type=IntegerType)
ElevensGame.attributes={ElevensGame_Board_9_, ElevensGame_win}

# Card_Interface class attributes and methods

# Relationships
ElevensGame_Deck: BinaryAssociation = BinaryAssociation(
    name="ElevensGame_Deck",
    ends={
        Property(name="deck0", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="elevensGame1", type=ElevensGame, multiplicity=Multiplicity(0, 1))
    }
)
ElevensGame_Player: BinaryAssociation = BinaryAssociation(
    name="ElevensGame_Player",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(0, 1)),
        Property(name="elevensGame3", type=ElevensGame, multiplicity=Multiplicity(0, 1))
    }
)
Interface_Deck: BinaryAssociation = BinaryAssociation(
    name="Interface_Deck",
    ends={
        Property(name="deck4", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="interface5", type=Card_Interface, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_V9YocEs6Eemxb9vmnJ3nLQ",
    types={Deck, Player, ElevensGame, Card_Interface, Board},
    associations={ElevensGame_Deck, ElevensGame_Player, Interface_Deck},
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