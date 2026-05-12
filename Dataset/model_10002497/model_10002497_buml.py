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
Kind: Enumeration = Enumeration(
    name="Kind",
    literals={
            
    }
)

# Classes
Game = Class(name="Game", is_abstract=True)
Player = Class(name="Player", is_abstract=True)
Card = Class(name="Card")

# Game class attributes and methods
Game_name: Property = Property(name="name", type=StringType)
Game.attributes={Game_name}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=StringType)
Card_kind: Property = Property(name="kind", type=Kind)
Card.attributes={Card_kind, Card_suit}

# Relationships
Player_Card: BinaryAssociation = BinaryAssociation(
    name="Player_Card",
    ends={
        Property(name="cards0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="player1", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Game_Player2: BinaryAssociation = BinaryAssociation(
    name="Game_Player2",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="game3", type=Game, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ba3e930e_5446_4d66_817b_9440122e2486",
    types={Game, Player, Card, Kind},
    associations={Player_Card, Game_Player2},
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