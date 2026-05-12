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
PlayerCPU_external = Class(name="PlayerCPU_external")
PlayerUser_external = Class(name="PlayerUser_external")
WAR = Class(name="WAR")
Deck = Class(name="Deck")
Card_Interface = Class(name="Card_Interface")
Class_ = Class(name="Class")
Players = Class(name="Players")
Function = Class(name="Function")

# PlayerCPU_external class attributes and methods

# PlayerUser_external class attributes and methods

# WAR class attributes and methods

# Deck class attributes and methods
Deck_topcard: Property = Property(name="topcard", type=IntegerType)
Deck_draw__: Property = Property(name="draw__", type=StringType)
Deck_shuffle__: Property = Property(name="shuffle__", type=StringType)
Deck_deck__: Property = Property(name="deck__", type=Deck)
Deck_isEmpty__: Property = Property(name="isEmpty__", type=BooleanType)
Deck.attributes={Deck_shuffle__, Deck_isEmpty__, Deck_deck__, Deck_draw__, Deck_topcard}

# Card_Interface class attributes and methods

# Class class attributes and methods

# Players class attributes and methods
Players_Player1: Property = Property(name="Player1", type=Card_Interface)
Players_Player2: Property = Property(name="Player2", type=Card_Interface)
Players.attributes={Players_Player2, Players_Player1}

# Function class attributes and methods
Function_removedCard: Property = Property(name="removedCard", type=IntegerType)
Function_Score: Property = Property(name="Score", type=IntegerType)
Function.attributes={Function_removedCard, Function_Score}

# Relationships
Deck_WAR: BinaryAssociation = BinaryAssociation(
    name="Deck_WAR",
    ends={
        Property(name="wAR0", type=WAR, multiplicity=Multiplicity(0, 1)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card2", type=Card_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="deck3", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
WAR_Players: BinaryAssociation = BinaryAssociation(
    name="WAR_Players",
    ends={
        Property(name="players4", type=Players, multiplicity=Multiplicity(0, 1)),
        Property(name="wAR5", type=WAR, multiplicity=Multiplicity(0, 1))
    }
)
Players_WAR: BinaryAssociation = BinaryAssociation(
    name="Players_WAR",
    ends={
        Property(name="wAR6", type=WAR, multiplicity=Multiplicity(0, 1)),
        Property(name="players7", type=Players, multiplicity=Multiplicity(0, 1))
    }
)
Function_Players: BinaryAssociation = BinaryAssociation(
    name="Function_Players",
    ends={
        Property(name="players28", type=Players, multiplicity=Multiplicity(0, 1)),
        Property(name="function9", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
Function_PlayerCPU: BinaryAssociation = BinaryAssociation(
    name="Function_PlayerCPU",
    ends={
        Property(name="playerCPU10", type=PlayerCPU_external, multiplicity=Multiplicity(0, 1)),
        Property(name="function11", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
Function_PlayerUser: BinaryAssociation = BinaryAssociation(
    name="Function_PlayerUser",
    ends={
        Property(name="playerUser12", type=PlayerUser_external, multiplicity=Multiplicity(0, 1)),
        Property(name="function13", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
Function_Card: BinaryAssociation = BinaryAssociation(
    name="Function_Card",
    ends={
        Property(name="card14", type=Card_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="function15", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Function: BinaryAssociation = BinaryAssociation(
    name="Deck_Function",
    ends={
        Property(name="function16", type=Function, multiplicity=Multiplicity(0, 1)),
        Property(name="deck17", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_752eb5e3_4158_4cd8_b653_bbf7ddfe4e70",
    types={PlayerCPU_external, PlayerUser_external, WAR, Deck, Card_Interface, Class_, Players, Function},
    associations={Deck_WAR, Deck_Card, WAR_Players, Players_WAR, Function_Players, Function_PlayerCPU, Function_PlayerUser, Function_Card, Deck_Function},
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