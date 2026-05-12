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
Elevens = Class(name="Elevens")
Class_ = Class(name="Class")
Player = Class(name="Player")
Deck = Class(name="Deck")
Cards = Class(name="Cards")

# Elevens class attributes and methods
Elevens_Player: Property = Property(name="Player", type=Player)
Elevens_Deck: Property = Property(name="Deck", type=Deck)
Elevens.attributes={Elevens_Player, Elevens_Deck}

# Class class attributes and methods

# Player class attributes and methods
Player_wins: Property = Property(name="wins", type=IntegerType)
Player_losses: Property = Property(name="losses", type=IntegerType)
Player_winRate: Property = Property(name="winRate", type=StringType)
Player.attributes={Player_wins, Player_losses, Player_winRate}

# Deck class attributes and methods
Deck_Cards: Property = Property(name="Cards", type=Cards)
Deck.attributes={Deck_Cards}

# Cards class attributes and methods
Cards_Suit: Property = Property(name="Suit", type=StringType)
Cards_Character: Property = Property(name="Character", type=StringType)
Cards.attributes={Cards_Suit, Cards_Character}

# Relationships
Elevens_Player: BinaryAssociation = BinaryAssociation(
    name="Elevens_Player",
    ends={
        Property(name="player0", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="elevens1", type=Elevens, multiplicity=Multiplicity(0, 1))
    }
)
Elevens_Deck: BinaryAssociation = BinaryAssociation(
    name="Elevens_Deck",
    ends={
        Property(name="deck2", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="elevens3", type=Elevens, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Cards: BinaryAssociation = BinaryAssociation(
    name="Deck_Cards",
    ends={
        Property(name="cards4", type=Cards, multiplicity=Multiplicity(0, 1)),
        Property(name="deck5", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_WkAOYEv8EemIEMlOKLl_tQ",
    types={Elevens, Class_, Player, Deck, Cards},
    associations={Elevens_Player, Elevens_Deck, Deck_Cards},
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