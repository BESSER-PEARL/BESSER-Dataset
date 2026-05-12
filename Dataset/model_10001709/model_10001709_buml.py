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
player_Actor = Class(name="player_Actor")
system__Actor = Class(name="system__Actor")
Store_UseCase = Class(name="Store_UseCase")
Game_Play_UseCase = Class(name="Game_Play_UseCase")
Main_Menu_UseCase = Class(name="Main_Menu_UseCase")
Selection_UseCase = Class(name="Selection_UseCase")
Splash_UseCase = Class(name="Splash_UseCase")
save_game_state__UseCase = Class(name="save_game_state__UseCase")
exit_game__UseCase = Class(name="exit_game__UseCase")
view_achievements_UseCase = Class(name="view_achievements_UseCase")
save_achievemnts_UseCase = Class(name="save_achievemnts_UseCase")
lock_unlock_UseCase = Class(name="lock_unlock_UseCase")
T = Class(name="T")
splash_anim_controller = Class(name="splash_anim_controller")

# player_Actor class attributes and methods

# system__Actor class attributes and methods

# Store_UseCase class attributes and methods

# Game_Play_UseCase class attributes and methods

# Main_Menu_UseCase class attributes and methods

# Selection_UseCase class attributes and methods

# Splash_UseCase class attributes and methods

# save_game_state__UseCase class attributes and methods

# exit_game__UseCase class attributes and methods

# view_achievements_UseCase class attributes and methods

# save_achievemnts_UseCase class attributes and methods

# lock_unlock_UseCase class attributes and methods

# T class attributes and methods

# splash_anim_controller class attributes and methods
splash_anim_controller_attribute: Property = Property(name="attribute", type=StringType)
splash_anim_controller.attributes={splash_anim_controller_attribute}

# Relationships
player_Splash: BinaryAssociation = BinaryAssociation(
    name="player_Splash",
    ends={
        Property(name="splash0", type=Splash_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player1", type=player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
player_Selection: BinaryAssociation = BinaryAssociation(
    name="player_Selection",
    ends={
        Property(name="selection2", type=Selection_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player3", type=player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
player_Main_Menu: BinaryAssociation = BinaryAssociation(
    name="player_Main_Menu",
    ends={
        Property(name="main_Menu4", type=Main_Menu_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player5", type=player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
player_Game_Play: BinaryAssociation = BinaryAssociation(
    name="player_Game_Play",
    ends={
        Property(name="game_Play6", type=Game_Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player7", type=player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
player_Store: BinaryAssociation = BinaryAssociation(
    name="player_Store",
    ends={
        Property(name="store8", type=Store_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player9", type=player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
player_view_achievements: BinaryAssociation = BinaryAssociation(
    name="player_view_achievements",
    ends={
        Property(name="view_achievements10", type=view_achievements_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player11", type=player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
system__Splash: BinaryAssociation = BinaryAssociation(
    name="system__Splash",
    ends={
        Property(name="splash12", type=Splash_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="system13", type=system__Actor, multiplicity=Multiplicity(0, 1))
    }
)
system__Selection: BinaryAssociation = BinaryAssociation(
    name="system__Selection",
    ends={
        Property(name="selection14", type=Selection_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="system15", type=system__Actor, multiplicity=Multiplicity(0, 1))
    }
)
system__exit_game: BinaryAssociation = BinaryAssociation(
    name="system__exit_game",
    ends={
        Property(name="exit_game16", type=exit_game__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="system17", type=system__Actor, multiplicity=Multiplicity(0, 1))
    }
)
system__save_game_state: BinaryAssociation = BinaryAssociation(
    name="system__save_game_state",
    ends={
        Property(name="save_game_state18", type=save_game_state__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="system19", type=system__Actor, multiplicity=Multiplicity(0, 1))
    }
)
system__save_achievemnts: BinaryAssociation = BinaryAssociation(
    name="system__save_achievemnts",
    ends={
        Property(name="save_achievemnts20", type=save_achievemnts_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="system21", type=system__Actor, multiplicity=Multiplicity(0, 1))
    }
)
lock_unlock_system: BinaryAssociation = BinaryAssociation(
    name="lock_unlock_system",
    ends={
        Property(name="system22", type=system__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="lock_unlock23", type=lock_unlock_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Q5RlICUgEeiYD9TOdwevwA",
    types={player_Actor, system__Actor, Store_UseCase, Game_Play_UseCase, Main_Menu_UseCase, Selection_UseCase, Splash_UseCase, save_game_state__UseCase, exit_game__UseCase, view_achievements_UseCase, save_achievemnts_UseCase, lock_unlock_UseCase, T, splash_anim_controller},
    associations={player_Splash, player_Selection, player_Main_Menu, player_Game_Play, player_Store, player_view_achievements, system__Splash, system__Selection, system__exit_game, system__save_game_state, system__save_achievemnts, lock_unlock_system},
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