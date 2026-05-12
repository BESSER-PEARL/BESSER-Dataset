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
BomberMan = Class(name="BomberMan")
Game = Class(name="Game")
Monster = Class(name="Monster")
GameMap = Class(name="GameMap")
PowerUps = Class(name="PowerUps")

# BomberMan class attributes and methods
BomberMan_points: Property = Property(name="points", type=IntegerType)
BomberMan_lives: Property = Property(name="lives", type=IntegerType)
BomberMan_location: Property = Property(name="location", type=StringType)
BomberMan.attributes={BomberMan_location, BomberMan_lives, BomberMan_points}

# Game class attributes and methods
Game_Timer: Property = Property(name="Timer", type=IntegerType)
Game.attributes={Game_Timer}

# Monster class attributes and methods
Monster_location: Property = Property(name="location", type=StringType)
Monster_type: Property = Property(name="type", type=StringType)
Monster_specilization: Property = Property(name="specilization", type=StringType)
Monster_lives: Property = Property(name="lives", type=IntegerType)
Monster.attributes={Monster_lives, Monster_type, Monster_location, Monster_specilization}

# GameMap class attributes and methods
GameMap_walls: Property = Property(name="walls", type=StringType)
GameMap_transitions: Property = Property(name="transitions", type=StringType)
GameMap_poerups: Property = Property(name="poerups", type=StringType)
GameMap.attributes={GameMap_walls, GameMap_poerups, GameMap_transitions}

# PowerUps class attributes and methods
PowerUps_locations: Property = Property(name="locations", type=StringType)
PowerUps_speciliaty: Property = Property(name="speciliaty", type=StringType)
PowerUps_points: Property = Property(name="points", type=IntegerType)
PowerUps.attributes={PowerUps_locations, PowerUps_points, PowerUps_speciliaty}

# Domain Model
domain_model = DomainModel(
    name="_79755ca5_7584_4f98_b5f8_de3b396bdca5",
    types={BomberMan, Game, Monster, GameMap, PowerUps},
    associations={},
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