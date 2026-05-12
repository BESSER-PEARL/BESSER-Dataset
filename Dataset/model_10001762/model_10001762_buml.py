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
Rank: Enumeration = Enumeration(
    name="Rank",
    literals={
            
    }
)

Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

# Classes
Blackjack = Class(name="Blackjack")
Deck = Class(name="Deck")
Card = Class(name="Card")

# Blackjack class attributes and methods

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=StringType)
Deck.attributes={Deck_cards}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=StringType)
Card_rank: Property = Property(name="rank", type=StringType)
Card.attributes={Card_rank, Card_suit}

# Domain Model
domain_model = DomainModel(
    name="_Tsd1gF5QEemkzeedQvutWw",
    types={Blackjack, Deck, Card, Rank, Suit},
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