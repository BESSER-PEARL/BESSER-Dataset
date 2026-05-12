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
Cards = Class(name="Cards")
Card = Class(name="Card")
Player = Class(name="Player")
Blackjack = Class(name="Blackjack")

# Cards class attributes and methods
Cards_color: Property = Property(name="color", type=StringType)
Cards_number: Property = Property(name="number", type=StringType)
Cards.attributes={Cards_color, Cards_number}

# Card class attributes and methods
Card_value_dict: Property = Property(name="value_dict", type=StringType)
Card.attributes={Card_value_dict}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_hand: Property = Property(name="hand", type=StringType)
Player.attributes={Player_hand, Player_name}

# Blackjack class attributes and methods
Blackjack_cards: Property = Property(name="cards", type=Cards)
Blackjack_players: Property = Property(name="players", type=StringType)
Blackjack_dealer: Property = Property(name="dealer", type=Player)
Blackjack.attributes={Blackjack_players, Blackjack_dealer, Blackjack_cards}

# Relationships
Card_Cards: BinaryAssociation = BinaryAssociation(
    name="Card_Cards",
    ends={
        Property(name="cards0", type=Cards, multiplicity=Multiplicity(0, 1)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 1))
    }
)
Card_Player: BinaryAssociation = BinaryAssociation(
    name="Card_Player",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(0, 9999)),
        Property(name="card3", type=Card, multiplicity=Multiplicity(0, 1))
    }
)
Player_Blackjack: BinaryAssociation = BinaryAssociation(
    name="Player_Blackjack",
    ends={
        Property(name="blackjack4", type=Blackjack, multiplicity=Multiplicity(0, 1)),
        Property(name="player5", type=Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_qtPLgFO_EeqK2M3E1LfZ7Q",
    types={Cards, Card, Player, Blackjack},
    associations={Card_Cards, Card_Player, Player_Blackjack},
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