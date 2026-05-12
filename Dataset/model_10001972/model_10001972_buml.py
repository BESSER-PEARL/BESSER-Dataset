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
ScoreType: Enumeration = Enumeration(
    name="ScoreType",
    literals={
            
    }
)

# Classes
Match = Class(name="Match")
Player = Class(name="Player")
Game = Class(name="Game")
Attempt = Class(name="Attempt")
FileImporter = Class(name="FileImporter")
InitialData = Class(name="InitialData")
Result = Class(name="Result")
Importer_Interface = Class(name="Importer_Interface")
BowlingGame = Class(name="BowlingGame")

# Match class attributes and methods
Match_date: Property = Property(name="date", type=StringType)
Match_name: Property = Property(name="name", type=StringType)
Match_players: Property = Property(name="players", type=StringType)
Match_winner: Property = Property(name="winner", type=Result)
Match.attributes={Match_winner, Match_players, Match_date, Match_name}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_totalScore: Property = Property(name="totalScore", type=IntegerType)
Player_games: Property = Property(name="games", type=Game)
Player.attributes={Player_totalScore, Player_name, Player_games}

# Game class attributes and methods
Game_number: Property = Property(name="number", type=IntegerType)
Game_score: Property = Property(name="score", type=IntegerType)
Game.attributes={Game_number, Game_score}

# Attempt class attributes and methods
Attempt_number: Property = Property(name="number", type=IntegerType)
Attempt_points: Property = Property(name="points", type=IntegerType)
Attempt.attributes={Attempt_points, Attempt_number}

# FileImporter class attributes and methods
FileImporter_INITIAL_DATAFILE: Property = Property(name="INITIAL_DATAFILE", type=StringType)
FileImporter.attributes={FileImporter_INITIAL_DATAFILE}

# InitialData class attributes and methods
InitialData_playerName: Property = Property(name="playerName", type=StringType)
InitialData_points: Property = Property(name="points", type=StringType)
InitialData.attributes={InitialData_playerName, InitialData_points}

# Result class attributes and methods
Result_player: Property = Property(name="player", type=StringType)
Result_score: Property = Property(name="score", type=IntegerType)
Result.attributes={Result_score, Result_player}

# Importer_Interface class attributes and methods

# BowlingGame class attributes and methods
BowlingGame_attempts: Property = Property(name="attempts", type=StringType)
BowlingGame_scoreType: Property = Property(name="scoreType", type=ScoreType)
BowlingGame_previousGame: Property = Property(name="previousGame", type=Game)
BowlingGame_nextGames: Property = Property(name="nextGames", type=StringType)
BowlingGame.attributes={BowlingGame_scoreType, BowlingGame_nextGames, BowlingGame_previousGame, BowlingGame_attempts}

# Domain Model
domain_model = DomainModel(
    name="_grOBAOs7EeiJfugOH9Y5Zg",
    types={Match, Player, Game, Attempt, FileImporter, InitialData, Result, Importer_Interface, BowlingGame, ScoreType},
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