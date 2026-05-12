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
State: Enumeration = Enumeration(
    name="State",
    literals={
            
    }
)

Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

Enumeration2: Enumeration = Enumeration(
    name="Enumeration2",
    literals={
            
    }
)

Role: Enumeration = Enumeration(
    name="Role",
    literals={
            
    }
)

NightAction: Enumeration = Enumeration(
    name="NightAction",
    literals={
            
    }
)

# Classes
BaseRole = Class(name="BaseRole")
Villager = Class(name="Villager")
Wolf = Class(name="Wolf")
Seer = Class(name="Seer")
Guardian = Class(name="Guardian")
Player = Class(name="Player")
Game = Class(name="Game")
Room = Class(name="Room")
ChatMessage = Class(name="ChatMessage")
SysMessage = Class(name="SysMessage")

# BaseRole class attributes and methods
BaseRole_role: Property = Property(name="role", type=Role)
BaseRole_appear_as: Property = Property(name="appear_as", type=Role)
BaseRole_night_action: Property = Property(name="night_action", type=NightAction)
BaseRole_wins_with: Property = Property(name="wins_with", type=Role)
BaseRole.attributes={BaseRole_role, BaseRole_appear_as, BaseRole_wins_with, BaseRole_night_action}

# Villager class attributes and methods

# Wolf class attributes and methods

# Seer class attributes and methods

# Guardian class attributes and methods

# Player class attributes and methods
Player_role: Property = Property(name="role", type=StringType)
Player_isAlive: Property = Property(name="isAlive", type=BooleanType)
Player_votes: Property = Property(name="votes", type=IntegerType)
Player_vote_for: Property = Property(name="vote_for", type=Player)
Player_night_target: Property = Property(name="night_target", type=Player)
Player.attributes={Player_night_target, Player_vote_for, Player_role, Player_isAlive, Player_votes}

# Game class attributes and methods
Game_turn_state: Property = Property(name="turn_state", type=State)
Game.attributes={Game_turn_state}

# Room class attributes and methods

# ChatMessage class attributes and methods

# SysMessage class attributes and methods

# Relationships
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="player0", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="game1", type=Game, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_84gCsE18Eeeu8_4LH_yuyg",
    types={BaseRole, Villager, Wolf, Seer, Guardian, Player, Game, Room, ChatMessage, SysMessage, State, Enumeration_, Enumeration2, Role, NightAction},
    associations={Game_Player},
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