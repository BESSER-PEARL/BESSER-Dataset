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
Executive = Class(name="Executive")
Table = Class(name="Table")
Deck = Class(name="Deck")
Stack = Class(name="Stack")
T = Class(name="T")
Player = Class(name="Player")
Tuple = Class(name="Tuple")
T1 = Class(name="T1")
T2 = Class(name="T2")
CasinoManager = Class(name="CasinoManager")
Queue = Class(name="Queue")
T3 = Class(name="T3")

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card_suit: Property = Property(name="suit", type=StringType)
Card.attributes={Card_value, Card_suit}

# Executive class attributes and methods

# Table class attributes and methods
Table_deck: Property = Property(name="deck", type=Deck)
Table_currPlayers: Property = Property(name="currPlayers", type=StringType)
Table.attributes={Table_currPlayers, Table_deck}

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=StringType)
Deck.attributes={Deck_cards}

# Stack class attributes and methods

# T class attributes and methods

# Player class attributes and methods

# Tuple class attributes and methods

# T1 class attributes and methods

# T2 class attributes and methods

# CasinoManager class attributes and methods
CasinoManager_table: Property = Property(name="table", type=Table)
CasinoManager_waitList: Property = Property(name="waitList", type=StringType)
CasinoManager.attributes={CasinoManager_waitList, CasinoManager_table}

# Queue class attributes and methods

# T3 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_V3_DgKnsEeeEQN1ZyOr__g",
    types={Card, Executive, Table, Deck, Stack, T, Player, Tuple, T1, T2, CasinoManager, Queue, T3},
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