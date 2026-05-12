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
Strategy1___Strategy2 = Class(name="Strategy1___Strategy2")
Deck = Class(name="Deck")
Card_Interface = Class(name="Card_Interface")
Players = Class(name="Players")
T = Class(name="T")
Driver = Class(name="Driver")

# Strategy1___Strategy2 class attributes and methods

# Deck class attributes and methods
Deck_shuffle__: Property = Property(name="shuffle__", type=StringType)
Deck_deck__: Property = Property(name="deck__", type=Deck)
Deck_isEmpty__: Property = Property(name="isEmpty__", type=BooleanType)
Deck.attributes={Deck_isEmpty__, Deck_deck__, Deck_shuffle__}

# Card_Interface class attributes and methods

# Players class attributes and methods
Players_Player1: Property = Property(name="Player1", type=Card_Interface)
Players_Player2: Property = Property(name="Player2", type=Card_Interface)
Players_Planet: Property = Property(name="Planet", type=Card_Interface)
Players.attributes={Players_Player1, Players_Planet, Players_Player2}

# T class attributes and methods

# Driver class attributes and methods
Driver_Score: Property = Property(name="Score", type=IntegerType)
Driver_removedCard: Property = Property(name="removedCard", type=IntegerType)
Driver.attributes={Driver_removedCard, Driver_Score}

# Relationships
Function_Players: BinaryAssociation = BinaryAssociation(
    name="Function_Players",
    ends={
        Property(name="Players8", type=Players, multiplicity=Multiplicity(0, 1)),
        Property(name="driver9", type=Driver, multiplicity=Multiplicity(0, 1))
    }
)
Function_Card: BinaryAssociation = BinaryAssociation(
    name="Function_Card",
    ends={
        Property(name="card10", type=Card_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="function11", type=Driver, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Function: BinaryAssociation = BinaryAssociation(
    name="Deck_Function",
    ends={
        Property(name="function12", type=Driver, multiplicity=Multiplicity(0, 1)),
        Property(name="deck13", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
Deck_WAR: BinaryAssociation = BinaryAssociation(
    name="Deck_WAR",
    ends={
        Property(name="Strategy1_20", type=Strategy1___Strategy2, multiplicity=Multiplicity(0, 1)),
        Property(name="Strategy1_21", type=Deck, multiplicity=Multiplicity(0, 1))
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
        Property(name="Strategy1___25", type=Strategy1___Strategy2, multiplicity=Multiplicity(0, 1))
    }
)
Players_WAR: BinaryAssociation = BinaryAssociation(
    name="Players_WAR",
    ends={
        Property(name="Strategy1_26", type=Strategy1___Strategy2, multiplicity=Multiplicity(0, 1)),
        Property(name="players7", type=Players, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bacc0d43_9c14_4512_b559_f8bda2fb9ca3",
    types={Strategy1___Strategy2, Deck, Card_Interface, Players, T, Driver},
    associations={Function_Players, Function_Card, Deck_Function, Deck_WAR, Deck_Card, WAR_Players, Players_WAR},
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