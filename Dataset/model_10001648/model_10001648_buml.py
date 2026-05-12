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
CardDeck = Class(name="CardDeck")

# Card class attributes and methods
Card_cardSuit: Property = Property(name="cardSuit", type=StringType)
Card_cardFace: Property = Property(name="cardFace", type=IntegerType)
Card.attributes={Card_cardFace, Card_cardSuit}

# CardDeck class attributes and methods
CardDeck_cards: Property = Property(name="cards", type=StringType)
CardDeck_suits: Property = Property(name="suits", type=StringType)
CardDeck.attributes={CardDeck_suits, CardDeck_cards}

# Relationships
CardDeck_Card: BinaryAssociation = BinaryAssociation(
    name="CardDeck_Card",
    ends={
        Property(name="CardDeck_Card_00", type=Card, multiplicity=Multiplicity(4, 52)),
        Property(name="Has1", type=CardDeck, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_LZ59sCh_Eem8L7GnWj5llQ",
    types={Card, CardDeck},
    associations={CardDeck_Card},
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