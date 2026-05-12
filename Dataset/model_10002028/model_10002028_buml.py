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
Creator = Class(name="Creator")
ComputerPlayer = Class(name="ComputerPlayer")
Banker = Class(name="Banker")
Business_Owner = Class(name="Business_Owner")
Interface_Interface = Class(name="Interface_Interface")
Human_Player_external = Class(name="Human_Player_external")
Cards_external = Class(name="Cards_external")

# Creator class attributes and methods
Creator_name: Property = Property(name="name", type=StringType)
Creator_money: Property = Property(name="money", type=FloatType)
Creator_currentBet: Property = Property(name="currentBet", type=FloatType)
Creator_folded: Property = Property(name="folded", type=BooleanType)
Creator.attributes={Creator_currentBet, Creator_name, Creator_folded, Creator_money}

# ComputerPlayer class attributes and methods
ComputerPlayer_difficulty: Property = Property(name="difficulty", type=IntegerType)
ComputerPlayer.attributes={ComputerPlayer_difficulty}

# Banker class attributes and methods
Banker__Card_cards_52_: Property = Property(name="_Card_cards_52_", type=IntegerType)
Banker.attributes={Banker__Card_cards_52_}

# Business_Owner class attributes and methods
Business_Owner__Card_cards_5_: Property = Property(name="_Card_cards_5_", type=IntegerType)
Business_Owner.attributes={Business_Owner__Card_cards_5_}

# Interface_Interface class attributes and methods

# Human_Player_external class attributes and methods

# Cards_external class attributes and methods

# Relationships
Player_ComputerPlayer: BinaryAssociation = BinaryAssociation(
    name="Player_ComputerPlayer",
    ends={
        Property(name="computerPlayer0", type=ComputerPlayer, multiplicity=Multiplicity(0, 1)),
        Property(name="player1", type=Creator, multiplicity=Multiplicity(0, 1))
    }
)
Player_Human_Player: BinaryAssociation = BinaryAssociation(
    name="Player_Human_Player",
    ends={
        Property(name="human_Player2", type=Human_Player_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player3", type=Creator, multiplicity=Multiplicity(0, 1))
    }
)
Cards_Hand: BinaryAssociation = BinaryAssociation(
    name="Cards_Hand",
    ends={
        Property(name="make_up_possible_hand4", type=Business_Owner, multiplicity=Multiplicity(0, 1)),
        Property(name="cards5", type=Cards_external, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kX8wMJCFEeW2I_OUujANxA",
    types={Creator, ComputerPlayer, Banker, Business_Owner, Interface_Interface, Human_Player_external, Cards_external, Enumeration_},
    associations={Player_ComputerPlayer, Player_Human_Player, Cards_Hand},
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