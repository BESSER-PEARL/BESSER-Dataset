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
User_Actor = Class(name="User_Actor")
Start_new_game_UseCase = Class(name="Start_new_game_UseCase")
Play_game_UseCase = Class(name="Play_game_UseCase")
View_high_score_UseCase = Class(name="View_high_score_UseCase")
GameSession = Class(name="GameSession")
Snake = Class(name="Snake")
Player = Class(name="Player")
FoodCell = Class(name="FoodCell")
MapCell = Class(name="MapCell", is_abstract=True)
WallCell = Class(name="WallCell")
Map = Class(name="Map")
EmptyCell = Class(name="EmptyCell")
Food = Class(name="Food")
Wall = Class(name="Wall")
SnakeBody = Class(name="SnakeBody")
Square = Class(name="Square")
Food1 = Class(name="Food1")
Snake1 = Class(name="Snake1")
Game = Class(name="Game")

# User_Actor class attributes and methods

# Start_new_game_UseCase class attributes and methods

# Play_game_UseCase class attributes and methods

# View_high_score_UseCase class attributes and methods

# GameSession class attributes and methods

# Snake class attributes and methods

# Player class attributes and methods

# FoodCell class attributes and methods

# MapCell class attributes and methods

# WallCell class attributes and methods

# Map class attributes and methods

# EmptyCell class attributes and methods

# Food class attributes and methods

# Wall class attributes and methods

# SnakeBody class attributes and methods

# Square class attributes and methods

# Food1 class attributes and methods

# Snake1 class attributes and methods

# Game class attributes and methods

# Relationships
User_Start_new_game: BinaryAssociation = BinaryAssociation(
    name="User_Start_new_game",
    ends={
        Property(name="start_new_game0", type=Start_new_game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Play_game: BinaryAssociation = BinaryAssociation(
    name="User_Play_game",
    ends={
        Property(name="play_game2", type=Play_game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_high_score: BinaryAssociation = BinaryAssociation(
    name="User_View_high_score",
    ends={
        Property(name="view_high_score4", type=View_high_score_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Map_Item: BinaryAssociation = BinaryAssociation(
    name="Map_Item",
    ends={
        Property(name="items6", type=MapCell, multiplicity=Multiplicity(0, 9999)),
        Property(name="map7", type=Map, multiplicity=Multiplicity(0, 1))
    }
)
GameSession_Map: BinaryAssociation = BinaryAssociation(
    name="GameSession_Map",
    ends={
        Property(name="map8", type=Map, multiplicity=Multiplicity(0, 1)),
        Property(name="gameSession9", type=GameSession, multiplicity=Multiplicity(0, 1))
    }
)
GameSession_Snake: BinaryAssociation = BinaryAssociation(
    name="GameSession_Snake",
    ends={
        Property(name="snake10", type=Snake, multiplicity=Multiplicity(1, 9999)),
        Property(name="gameSession11", type=GameSession, multiplicity=Multiplicity(0, 1))
    }
)
GameSession_Player: BinaryAssociation = BinaryAssociation(
    name="GameSession_Player",
    ends={
        Property(name="player12", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="gameSession13", type=GameSession, multiplicity=Multiplicity(0, 1))
    }
)
Wall_WallCell: BinaryAssociation = BinaryAssociation(
    name="Wall_WallCell",
    ends={
        Property(name="wallCell14", type=WallCell, multiplicity=Multiplicity(0, 1)),
        Property(name="wall15", type=Wall, multiplicity=Multiplicity(0, 1))
    }
)
Food_FoodCell: BinaryAssociation = BinaryAssociation(
    name="Food_FoodCell",
    ends={
        Property(name="foodCell16", type=FoodCell, multiplicity=Multiplicity(0, 1)),
        Property(name="food17", type=Food, multiplicity=Multiplicity(0, 1))
    }
)
Player_Snake: BinaryAssociation = BinaryAssociation(
    name="Player_Snake",
    ends={
        Property(name="snake18", type=Snake, multiplicity=Multiplicity(0, 1)),
        Property(name="player19", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Snake_SnakeBody: BinaryAssociation = BinaryAssociation(
    name="Snake_SnakeBody",
    ends={
        Property(name="snakeBody20", type=SnakeBody, multiplicity=Multiplicity(1, 9999)),
        Property(name="snake21", type=Snake, multiplicity=Multiplicity(0, 1))
    }
)
MapCell_SnakeBody: BinaryAssociation = BinaryAssociation(
    name="MapCell_SnakeBody",
    ends={
        Property(name="snakeBody22", type=SnakeBody, multiplicity=Multiplicity(0, 1)),
        Property(name="mapCell23", type=MapCell, multiplicity=Multiplicity(1, 1))
    }
)
Game__Snake: BinaryAssociation = BinaryAssociation(
    name="Game__Snake",
    ends={
        Property(name="snake24", type=Snake1, multiplicity=Multiplicity(0, 1)),
        Property(name="game25", type=Game, multiplicity=Multiplicity(0, 1))
    }
)
Game__Square: BinaryAssociation = BinaryAssociation(
    name="Game__Square",
    ends={
        Property(name="square26", type=Square, multiplicity=Multiplicity(0, 1)),
        Property(name="game27", type=Snake1, multiplicity=Multiplicity(0, 1))
    }
)
Square__Food: BinaryAssociation = BinaryAssociation(
    name="Square__Food",
    ends={
        Property(name="food28", type=Food1, multiplicity=Multiplicity(0, 1)),
        Property(name="square29", type=Square, multiplicity=Multiplicity(0, 1))
    }
)
Game__Food: BinaryAssociation = BinaryAssociation(
    name="Game__Food",
    ends={
        Property(name="food30", type=Food1, multiplicity=Multiplicity(0, 1)),
        Property(name="game31", type=Game, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a4173745_1fd1_417c_b1be_5627f9bc9bf1",
    types={User_Actor, Start_new_game_UseCase, Play_game_UseCase, View_high_score_UseCase, GameSession, Snake, Player, FoodCell, MapCell, WallCell, Map, EmptyCell, Food, Wall, SnakeBody, Square, Food1, Snake1, Game, Enumeration_},
    associations={User_Start_new_game, User_Play_game, User_View_high_score, Map_Item, GameSession_Map, GameSession_Snake, GameSession_Player, Wall_WallCell, Food_FoodCell, Player_Snake, Snake_SnakeBody, MapCell_SnakeBody, Game__Snake, Game__Square, Square__Food, Game__Food},
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