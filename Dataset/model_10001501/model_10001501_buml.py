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
FortuneTeller = Class(name="FortuneTeller")
Card___Abstract__ = Class(name="Card___Abstract__")
TarotCard___Card = Class(name="TarotCard___Card")

# Deck class attributes and methods
Deck__deck: Property = Property(name="_deck", type=StringType)
Deck.attributes={Deck__deck}

# FortuneTeller class attributes and methods
FortuneTeller__tarotDeck: Property = Property(name="_tarotDeck", type=Deck)
FortuneTeller.attributes={FortuneTeller__tarotDeck}

# Card___Abstract__ class attributes and methods
Card___Abstract____id: Property = Property(name="_id", type=IntegerType)
Card___Abstract__.attributes={Card___Abstract____id}

# TarotCard___Card class attributes and methods
TarotCard___Card__id: Property = Property(name="_id", type=IntegerType)
TarotCard___Card__fileName: Property = Property(name="_fileName", type=StringType)
TarotCard___Card__fortunes: Property = Property(name="_fortunes", type=StringType)
TarotCard___Card.attributes={TarotCard___Card__fortunes, TarotCard___Card__id, TarotCard___Card__fileName}

# Relationships
Card___Abstract___Deck: BinaryAssociation = BinaryAssociation(
    name="Card___Abstract___Deck",
    ends={
        Property(name="deck0", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="card___Abstract__1", type=Card___Abstract__, multiplicity=Multiplicity(0, 1))
    }
)
FortuneTeller_Deck: BinaryAssociation = BinaryAssociation(
    name="FortuneTeller_Deck",
    ends={
        Property(name="deck2", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="fortuneTeller3", type=FortuneTeller, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_BLrH4MAXEeeEXb8Dudo6PQ",
    types={Deck, FortuneTeller, Card___Abstract__, TarotCard___Card},
    associations={Card___Abstract___Deck, FortuneTeller_Deck},
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