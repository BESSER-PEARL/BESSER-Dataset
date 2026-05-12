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
Cards_Suit: Enumeration = Enumeration(
    name="Cards_Suit",
    literals={
            
    }
)

Cards_Rank: Enumeration = Enumeration(
    name="Cards_Rank",
    literals={
            
    }
)

# Classes
Cards_Card = Class(name="Cards_Card")
Cards_StarndardDeck = Class(name="Cards_StarndardDeck")
Cards_Deck_Interface = Class(name="Cards_Deck_Interface")

# Cards_Card class attributes and methods
Cards_Card_rank: Property = Property(name="rank", type=Cards_Rank)
Cards_Card_suit: Property = Property(name="suit", type=Cards_Suit)
Cards_Card.attributes={Cards_Card_suit, Cards_Card_rank}

# Cards_StarndardDeck class attributes and methods
Cards_StarndardDeck_rand: Property = Property(name="rand", type=StringType)
Cards_StarndardDeck_cards: Property = Property(name="cards", type=Cards_Card)
Cards_StarndardDeck.attributes={Cards_StarndardDeck_rand, Cards_StarndardDeck_cards}

# Cards_Deck_Interface class attributes and methods

# Relationships
StarndardDeck_Card: BinaryAssociation = BinaryAssociation(
    name="StarndardDeck_Card",
    ends={
        Property(name="card0", type=Cards_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="starndardDeck1", type=Cards_StarndardDeck, multiplicity=Multiplicity(52, 52))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_GVEcwCNCEeisAYMSV00L2Q",
    types={Cards_Card, Cards_StarndardDeck, Cards_Deck_Interface, Cards_Suit, Cards_Rank},
    associations={StarndardDeck_Card},
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