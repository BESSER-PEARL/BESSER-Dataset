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
MemoryGame_Card = Class(name="MemoryGame_Card")
MemoryGame_Deck = Class(name="MemoryGame_Deck")
Player_Actor = Class(name="Player_Actor")
Begin_Game_UseCase = Class(name="Begin_Game_UseCase")
Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase = Class(name="Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase")
Shuffle_Deck__Restart_Game__UseCase = Class(name="Shuffle_Deck__Restart_Game__UseCase")
Quit_UseCase = Class(name="Quit_UseCase")
Change_Deck__Image_Changes__UseCase = Class(name="Change_Deck__Image_Changes__UseCase")

# MemoryGame_Card class attributes and methods
MemoryGame_Card_id: Property = Property(name="id", type=IntegerType)
MemoryGame_Card_image: Property = Property(name="image", type=StringType)
MemoryGame_Card_isShowing: Property = Property(name="isShowing", type=BooleanType)
MemoryGame_Card_deck: Property = Property(name="deck", type=MemoryGame_Deck)
MemoryGame_Card_position: Property = Property(name="position", type=IntegerType)
MemoryGame_Card.attributes={MemoryGame_Card_id, MemoryGame_Card_position, MemoryGame_Card_isShowing, MemoryGame_Card_deck, MemoryGame_Card_image}

# MemoryGame_Deck class attributes and methods
MemoryGame_Deck_id: Property = Property(name="id", type=IntegerType)
MemoryGame_Deck_image: Property = Property(name="image", type=StringType)
MemoryGame_Deck_cards: Property = Property(name="cards", type=MemoryGame_Card)
MemoryGame_Deck.attributes={MemoryGame_Deck_cards, MemoryGame_Deck_id, MemoryGame_Deck_image}

# Player_Actor class attributes and methods

# Begin_Game_UseCase class attributes and methods

# Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase class attributes and methods

# Shuffle_Deck__Restart_Game__UseCase class attributes and methods

# Quit_UseCase class attributes and methods

# Change_Deck__Image_Changes__UseCase class attributes and methods

# Relationships
Player_Change_Deck__Image_Changes_: BinaryAssociation = BinaryAssociation(
    name="Player_Change_Deck__Image_Changes_",
    ends={
        Property(name="change_Deck__Image_Changes_10", type=Change_Deck__Image_Changes__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player11", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card0", type=MemoryGame_Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck1", type=MemoryGame_Deck, multiplicity=Multiplicity(1, 1))
    }
)
Player_Start_New_Game: BinaryAssociation = BinaryAssociation(
    name="Player_Start_New_Game",
    ends={
        Property(name="start_New_Game2", type=Begin_Game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player3", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch: BinaryAssociation = BinaryAssociation(
    name="Player_Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch",
    ends={
        Property(name="match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch4", type=Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player5", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Shuffle_Deck__Start_New_Game_: BinaryAssociation = BinaryAssociation(
    name="Player_Shuffle_Deck__Start_New_Game_",
    ends={
        Property(name="shuffle_Deck__Start_New_Game_6", type=Shuffle_Deck__Restart_Game__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player7", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Quit: BinaryAssociation = BinaryAssociation(
    name="Player_Quit",
    ends={
        Property(name="quit8", type=Quit_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player9", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_1FQzgM5rEeeMV96X50GAvA",
    types={MemoryGame_Card, MemoryGame_Deck, Player_Actor, Begin_Game_UseCase, Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase, Shuffle_Deck__Restart_Game__UseCase, Quit_UseCase, Change_Deck__Image_Changes__UseCase},
    associations={Player_Change_Deck__Image_Changes_, Deck_Card, Player_Start_New_Game, Player_Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch, Player_Shuffle_Deck__Start_New_Game_, Player_Quit},
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