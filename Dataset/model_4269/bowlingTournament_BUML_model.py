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
TournamentType: Enumeration = Enumeration(
    name="TournamentType",
    literals={
            EnumerationLiteral(name="Pro"),
			EnumerationLiteral(name="Amateur")
    }
)

# Classes
bowlingTournament_League = Class(name="bowlingTournament::League")
bowlingTournament_Game = Class(name="bowlingTournament::Game")
bowlingTournament_Player = Class(name="bowlingTournament::Player")
bowlingTournament_Tournament = Class(name="bowlingTournament::Tournament")
bowlingTournament_Matchup = Class(name="bowlingTournament::Matchup")

# bowlingTournament_League class attributes and methods
bowlingTournament_League_name: Property = Property(name="name", type=StringType)
bowlingTournament_League.attributes={bowlingTournament_League_name}

# bowlingTournament_Game class attributes and methods
bowlingTournament_Game_frames: Property = Property(name="frames", type=IntegerType)
bowlingTournament_Game.attributes={bowlingTournament_Game_frames}

# bowlingTournament_Player class attributes and methods
bowlingTournament_Player_name: Property = Property(name="name", type=StringType)
bowlingTournament_Player_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowlingTournament_Player_height: Property = Property(name="height", type=FloatType)
bowlingTournament_Player_isProfessional: Property = Property(name="isProfessional", type=BooleanType)
bowlingTournament_Player.attributes={bowlingTournament_Player_height, bowlingTournament_Player_dateOfBirth, bowlingTournament_Player_isProfessional, bowlingTournament_Player_name}

# bowlingTournament_Tournament class attributes and methods
bowlingTournament_Tournament_type: Property = Property(name="type", type=StringType)
bowlingTournament_Tournament.attributes={bowlingTournament_Tournament_type}

# bowlingTournament_Matchup class attributes and methods

# Relationships
league2: BinaryAssociation = BinaryAssociation(
    name="league2",
    ends={
        Property(name="bowlingTournament_League4", type=bowlingTournament_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowlingTournament_Tournament3", type=bowlingTournament_League, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
games5: BinaryAssociation = BinaryAssociation(
    name="games5",
    ends={
        Property(name="Game", type=bowlingTournament_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchup", type=bowlingTournament_Game, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
player6: BinaryAssociation = BinaryAssociation(
    name="player6",
    ends={
        Property(name="bowlingTournament_Player7", type=bowlingTournament_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="bowlingTournament_Game", type=bowlingTournament_Player, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matchup8: BinaryAssociation = BinaryAssociation(
    name="matchup8",
    ends={
        Property(name="Matchup", type=bowlingTournament_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games", type=bowlingTournament_Matchup, multiplicity=Multiplicity(0, 1))
    }
)
player0: BinaryAssociation = BinaryAssociation(
    name="player0",
    ends={
        Property(name="bowlingTournament_Player", type=bowlingTournament_League, multiplicity=Multiplicity(1, 1)),
        Property(name="bowlingTournament_League", type=bowlingTournament_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matchups1: BinaryAssociation = BinaryAssociation(
    name="matchups1",
    ends={
        Property(name="bowlingTournament_Matchup", type=bowlingTournament_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowlingTournament_Tournament", type=bowlingTournament_Matchup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowlingTournament",
    types={bowlingTournament_League, bowlingTournament_Game, bowlingTournament_Player, bowlingTournament_Tournament, bowlingTournament_Matchup, TournamentType},
    associations={league2, games5, player6, matchup8, player0, matchups1},
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