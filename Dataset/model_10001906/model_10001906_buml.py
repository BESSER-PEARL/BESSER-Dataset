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
Deck = Class(name="Deck")
Card = Class(name="Card")

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck.attributes={Deck_deck}

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card_suit: Property = Property(name="suit", type=IntegerType)
Card_color: Property = Property(name="color", type=BooleanType)
Card.attributes={Card_suit, Card_color, Card_value}

# Relationships
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(0, 1)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_cUZ4MEdFEemB7r6RYSs12w",
    types={Deck, Card},
    associations={Deck_Card},
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