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
Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

CardValue: Enumeration = Enumeration(
    name="CardValue",
    literals={
            
    }
)

# Classes
User_Actor = Class(name="User_Actor")
Shuffle_Deck_UseCase = Class(name="Shuffle_Deck_UseCase")
Show_Deck_UseCase = Class(name="Show_Deck_UseCase")
Deal_a_Card_UseCase = Class(name="Deal_a_Card_UseCase")
Make_Move_UseCase = Class(name="Make_Move_UseCase")
Current_onto_Previous_UseCase = Class(name="Current_onto_Previous_UseCase")
Current_over_two_UseCase = Class(name="Current_over_two_UseCase")
Amalgamate_UseCase = Class(name="Amalgamate_UseCase")
Play_for_Me_UseCase = Class(name="Play_for_Me_UseCase")
Play_Once_UseCase = Class(name="Play_Once_UseCase")
Play_Multiple_Times_UseCase = Class(name="Play_Multiple_Times_UseCase")
Show_Top_Results_UseCase = Class(name="Show_Top_Results_UseCase")
Deck = Class(name="Deck")
Card = Class(name="Card")
Application = Class(name="Application")

# User_Actor class attributes and methods

# Shuffle_Deck_UseCase class attributes and methods

# Show_Deck_UseCase class attributes and methods

# Deal_a_Card_UseCase class attributes and methods

# Make_Move_UseCase class attributes and methods

# Current_onto_Previous_UseCase class attributes and methods

# Current_over_two_UseCase class attributes and methods

# Amalgamate_UseCase class attributes and methods

# Play_for_Me_UseCase class attributes and methods

# Play_Once_UseCase class attributes and methods

# Play_Multiple_Times_UseCase class attributes and methods

# Show_Top_Results_UseCase class attributes and methods

# Deck class attributes and methods
Deck__cards__: Property = Property(name="_cards__", type=Card)
Deck_scan: Property = Property(name="scan", type=StringType)
Deck.attributes={Deck__cards__, Deck_scan}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=Suit)
Card_cardValue: Property = Property(name="cardValue", type=CardValue)
Card.attributes={Card_cardValue, Card_suit}

# Application class attributes and methods
Application_scan: Property = Property(name="scan", type=StringType)
Application_deck: Property = Property(name="deck", type=Deck)
Application.attributes={Application_scan, Application_deck}

# Relationships
Make_MOve_Current_onto_Previous: BinaryAssociation = BinaryAssociation(
    name="Make_MOve_Current_onto_Previous",
    ends={
        Property(name="current_onto_Previous0", type=Current_onto_Previous_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="make_MOve1", type=Make_Move_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Make_MOve_Current_over_two: BinaryAssociation = BinaryAssociation(
    name="Make_MOve_Current_over_two",
    ends={
        Property(name="current_over_two2", type=Current_over_two_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="make_MOve3", type=Make_Move_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Make_MOve_Amalgamate: BinaryAssociation = BinaryAssociation(
    name="Make_MOve_Amalgamate",
    ends={
        Property(name="amalgamate4", type=Amalgamate_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="make_MOve5", type=Make_Move_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User_Make_MOve: BinaryAssociation = BinaryAssociation(
    name="User_Make_MOve",
    ends={
        Property(name="make_MOve6", type=Make_Move_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Deal_a_Card: BinaryAssociation = BinaryAssociation(
    name="User_Deal_a_Card",
    ends={
        Property(name="deal_a_Card8", type=Deal_a_Card_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Show_Deck: BinaryAssociation = BinaryAssociation(
    name="User_Show_Deck",
    ends={
        Property(name="show_Deck10", type=Show_Deck_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Shuffle_Deck: BinaryAssociation = BinaryAssociation(
    name="User_Shuffle_Deck",
    ends={
        Property(name="shuffle_Deck12", type=Shuffle_Deck_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Play_for_Me: BinaryAssociation = BinaryAssociation(
    name="User_Play_for_Me",
    ends={
        Property(name="play_for_Me14", type=Play_for_Me_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user15", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Play_for_Me_Play_Once: BinaryAssociation = BinaryAssociation(
    name="Play_for_Me_Play_Once",
    ends={
        Property(name="play_Once16", type=Play_Once_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="play_for_Me17", type=Play_for_Me_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Play_for_Me_Play_Multiple_Times: BinaryAssociation = BinaryAssociation(
    name="Play_for_Me_Play_Multiple_Times",
    ends={
        Property(name="play_Multiple_Times18", type=Play_Multiple_Times_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="play_for_Me19", type=Play_for_Me_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User_Show_Top_Results: BinaryAssociation = BinaryAssociation(
    name="User_Show_Top_Results",
    ends={
        Property(name="show_Top_Results20", type=Show_Top_Results_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user21", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_u6YjQFR_Eei2efM7H4gIXw",
    types={User_Actor, Shuffle_Deck_UseCase, Show_Deck_UseCase, Deal_a_Card_UseCase, Make_Move_UseCase, Current_onto_Previous_UseCase, Current_over_two_UseCase, Amalgamate_UseCase, Play_for_Me_UseCase, Play_Once_UseCase, Play_Multiple_Times_UseCase, Show_Top_Results_UseCase, Deck, Card, Application, Suit, CardValue},
    associations={Make_MOve_Current_onto_Previous, Make_MOve_Current_over_two, Make_MOve_Amalgamate, User_Make_MOve, User_Deal_a_Card, User_Show_Deck, User_Shuffle_Deck, User_Play_for_Me, Play_for_Me_Play_Once, Play_for_Me_Play_Multiple_Times, User_Show_Top_Results},
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