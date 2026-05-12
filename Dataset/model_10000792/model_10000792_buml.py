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
Blackjack = Class(name="Blackjack")
Player = Class(name="Player")
Dealer = Class(name="Dealer")
Card = Class(name="Card")
BlackjackDriver = Class(name="BlackjackDriver")
BlackjackGUI = Class(name="BlackjackGUI")
JFrame = Class(name="JFrame")

# Blackjack class attributes and methods
Blackjack_players: Property = Property(name="players", type=IntegerType)
Blackjack_count: Property = Property(name="count", type=IntegerType)
Blackjack_playerName: Property = Property(name="playerName", type=StringType)
Blackjack_hand__: Property = Property(name="hand__", type=Card)
Blackjack.attributes={Blackjack_hand__, Blackjack_count, Blackjack_playerName, Blackjack_players}

# Player class attributes and methods
Player_totalAmount: Property = Property(name="totalAmount", type=IntegerType)
Player.attributes={Player_totalAmount}

# Dealer class attributes and methods

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_rank: Property = Property(name="rank", type=IntegerType)
Card.attributes={Card_suit, Card_rank, Card_value}

# BlackjackDriver class attributes and methods

# BlackjackGUI class attributes and methods

# JFrame class attributes and methods

# Relationships
Blackjack_Card: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Card",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjack1", type=Blackjack, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6126ba23_3f56_4df8_9646_91c5c5dab28d",
    types={Blackjack, Player, Dealer, Card, BlackjackDriver, BlackjackGUI, JFrame},
    associations={Blackjack_Card},
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