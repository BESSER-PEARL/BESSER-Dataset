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
Timer = Class(name="Timer")
Game = Class(name="Game")
MineField = Class(name="MineField")
Class_ = Class(name="Class")
Position = Class(name="Position")
Chat = Class(name="Chat")

# Timer class attributes and methods
Timer_start: Property = Property(name="start", type=IntegerType)
Timer_ticks: Property = Property(name="ticks", type=IntegerType)
Timer.attributes={Timer_start, Timer_ticks}

# Game class attributes and methods
Game_time_keeper: Property = Property(name="time_keeper", type=Timer)
Game_mine_field: Property = Property(name="mine_field", type=MineField)
Game_score: Property = Property(name="score", type=IntegerType)
Game.attributes={Game_mine_field, Game_score, Game_time_keeper}

# MineField class attributes and methods
MineField_grid: Property = Property(name="grid", type=StringType)
MineField_height: Property = Property(name="height", type=IntegerType)
MineField_width: Property = Property(name="width", type=IntegerType)
MineField.attributes={MineField_height, MineField_grid, MineField_width}

# Class class attributes and methods

# Position class attributes and methods
Position_x: Property = Property(name="x", type=IntegerType)
Position_y: Property = Property(name="y", type=IntegerType)
Position_has_flag: Property = Property(name="has_flag", type=BooleanType)
Position_is_hidden: Property = Property(name="is_hidden", type=BooleanType)
Position.attributes={Position_is_hidden, Position_y, Position_x, Position_has_flag}

# Chat class attributes and methods
Chat_commands: Property = Property(name="commands", type=StringType)
Chat_username: Property = Property(name="username", type=StringType)
Chat.attributes={Chat_commands, Chat_username}

# Relationships
Game_Timer: BinaryAssociation = BinaryAssociation(
    name="Game_Timer",
    ends={
        Property(name="timer0", type=Timer, multiplicity=Multiplicity(0, 1)),
        Property(name="game1", type=Game, multiplicity=Multiplicity(0, 1))
    }
)
Game_MineField: BinaryAssociation = BinaryAssociation(
    name="Game_MineField",
    ends={
        Property(name="mineField2", type=MineField, multiplicity=Multiplicity(0, 1)),
        Property(name="game3", type=Game, multiplicity=Multiplicity(0, 1))
    }
)
MineField_Position: BinaryAssociation = BinaryAssociation(
    name="MineField_Position",
    ends={
        Property(name="position4", type=Position, multiplicity=Multiplicity(0, 1)),
        Property(name="mineField5", type=MineField, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__TOi0LSBEee7sYPkE4_GPA",
    types={Timer, Game, MineField, Class_, Position, Chat},
    associations={Game_Timer, Game_MineField, MineField_Position},
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