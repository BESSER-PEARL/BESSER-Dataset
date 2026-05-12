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
Hand = Class(name="Hand")
blackjackHand = Class(name="blackjackHand")
Blackjack = Class(name="Blackjack")
Deck = Class(name="Deck")
blackjackCard = Class(name="blackjackCard")
Class_ = Class(name="Class")
Class2 = Class(name="Class2")

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=IntegerType)
Card_face: Property = Property(name="face", type=IntegerType)
Card.attributes={Card_suit, Card_face}

# Hand class attributes and methods

# blackjackHand class attributes and methods

# Blackjack class attributes and methods

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck.attributes={Deck_deck}

# blackjackCard class attributes and methods

# Class class attributes and methods

# Class2 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_4SlBYEc7EeiOybRP6Wy3kg",
    types={Card, Hand, blackjackHand, Blackjack, Deck, blackjackCard, Class_, Class2},
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