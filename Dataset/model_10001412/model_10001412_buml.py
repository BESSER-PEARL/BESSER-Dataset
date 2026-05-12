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
Main = Class(name="Main")
Blackjack = Class(name="Blackjack")
InputValidation = Class(name="InputValidation")
Account = Class(name="Account")
Player = Class(name="Player")
Deck = Class(name="Deck")
Cards = Class(name="Cards")

# Main class attributes and methods

# Blackjack class attributes and methods

# InputValidation class attributes and methods

# Account class attributes and methods
Account_int: Property = Property(name="int", type=StringType)
Account_string: Property = Property(name="string", type=StringType)
Account_int1: Property = Property(name="int1", type=StringType)
Account.attributes={Account_string, Account_int1, Account_int}

# Player class attributes and methods
Player_int: Property = Property(name="int", type=StringType)
Player_int1: Property = Property(name="int1", type=StringType)
Player_Deck: Property = Property(name="Deck", type=StringType)
Player_Card: Property = Property(name="Card", type=StringType)
Player.attributes={Player_Deck, Player_int1, Player_int, Player_Card}

# Deck class attributes and methods
Deck_int: Property = Property(name="int", type=StringType)
Deck.attributes={Deck_int}

# Cards class attributes and methods
Cards_string: Property = Property(name="string", type=StringType)
Cards_int: Property = Property(name="int", type=StringType)
Cards_int1: Property = Property(name="int1", type=StringType)
Cards_bool: Property = Property(name="bool", type=StringType)
Cards.attributes={Cards_bool, Cards_string, Cards_int, Cards_int1}

# Relationships
Deck_Cards: BinaryAssociation = BinaryAssociation(
    name="Deck_Cards",
    ends={
        Property(name="cards0", type=Cards, multiplicity=Multiplicity(0, 1)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5M2bIOHLEee1VcqWCkiVQg",
    types={Main, Blackjack, InputValidation, Account, Player, Deck, Cards},
    associations={Deck_Cards},
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