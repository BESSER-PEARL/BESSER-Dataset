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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Card = Class(name="Card")
Deck = Class(name="Deck")
Hand = Class(name="Hand")
CustomException_CardException = Class(name="CustomException_CardException")
CustomException_DeckOrHandEmptyException = Class(name="CustomException_DeckOrHandEmptyException")
CustomException_InvalidCardException = Class(name="CustomException_InvalidCardException")
CardPlayer = Class(name="CardPlayer", is_abstract=True)
CardGame = Class(name="CardGame", is_abstract=True)
CardPlayer__ = Class(name="CardPlayer__")

# Card class attributes and methods
Card_Suit: Property = Property(name="Suit", type=Enumeration_)
Card_Rank: Property = Property(name="Rank", type=IntegerType)
Card.attributes={Card_Suit, Card_Rank}

# Deck class attributes and methods
Deck_CardsList: Property = Property(name="CardsList", type=StringType)
Deck.attributes={Deck_CardsList}

# Hand class attributes and methods
Hand_HandOfCards: Property = Property(name="HandOfCards", type=StringType)
Hand.attributes={Hand_HandOfCards}

# CustomException_CardException class attributes and methods

# CustomException_DeckOrHandEmptyException class attributes and methods

# CustomException_InvalidCardException class attributes and methods

# CardPlayer class attributes and methods

# CardGame class attributes and methods

# CardPlayer__ class attributes and methods

# Relationships
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="Deck_Card_00", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="Deck_Card_11", type=Deck, multiplicity=Multiplicity(0, 9999))
    }
)
Hand_Card: BinaryAssociation = BinaryAssociation(
    name="Hand_Card",
    ends={
        Property(name="Hand_Card_02", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="Hand_Card_13", type=Hand, multiplicity=Multiplicity(0, 9999))
    }
)
CardPlayer_Hand: BinaryAssociation = BinaryAssociation(
    name="CardPlayer_Hand",
    ends={
        Property(name="CardPlayer_Hand_04", type=Hand, multiplicity=Multiplicity(0, 9999)),
        Property(name="CardPlayer_Hand_15", type=CardPlayer, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kKfeADxUEei384rcaJKdxw",
    types={Card, Deck, Hand, CustomException_CardException, CustomException_DeckOrHandEmptyException, CustomException_InvalidCardException, CardPlayer, CardGame, CardPlayer__, Enumeration_},
    associations={Deck_Card, Hand_Card, CardPlayer_Hand},
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