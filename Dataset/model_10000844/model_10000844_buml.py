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
Operation: Enumeration = Enumeration(
    name="Operation",
    literals={
            
    }
)

Kind: Enumeration = Enumeration(
    name="Kind",
    literals={
            
    }
)

# Classes
Deck = Class(name="Deck")
Player = Class(name="Player", is_abstract=True)
Card = Class(name="Card")

# Deck class attributes and methods

# Player class attributes and methods

# Card class attributes and methods
Card_operation: Property = Property(name="operation", type=StringType)
Card_kind: Property = Property(name="kind", type=Kind)
Card.attributes={Card_operation, Card_kind}

# Relationships
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="cards0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="players2", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="Decks3", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Player_Card: BinaryAssociation = BinaryAssociation(
    name="Player_Card",
    ends={
        Property(name="cards4", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="player5", type=Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_67a9b95d_4622_4182_98b3_4d347330f691",
    types={Deck, Player, Card, Operation, Kind},
    associations={Deck_Card, Game_Player, Player_Card},
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