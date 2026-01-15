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
bowling_Tournament = Class(name="bowling::Tournament")
bowling_Matchup = Class(name="bowling::Matchup")
bowling_Player = Class(name="bowling::Player")
bowling_Game = Class(name="bowling::Game")
bowling_League = Class(name="bowling::League")

# bowling_Tournament class attributes and methods
bowling_Tournament_type: Property = Property(name="type", type=StringType)
bowling_Tournament.attributes={bowling_Tournament_type}

# bowling_Matchup class attributes and methods

# bowling_Player class attributes and methods
bowling_Player_name: Property = Property(name="name", type=StringType)
bowling_Player_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowling_Player_isProfessional: Property = Property(name="isProfessional", type=BooleanType)
bowling_Player_height: Property = Property(name="height", type=FloatType)
bowling_Player.attributes={bowling_Player_name, bowling_Player_isProfessional, bowling_Player_dateOfBirth, bowling_Player_height}

# bowling_Game class attributes and methods
bowling_Game_frames: Property = Property(name="frames", type=IntegerType)
bowling_Game.attributes={bowling_Game_frames}

# bowling_League class attributes and methods
bowling_League_name: Property = Property(name="name", type=StringType)
bowling_League.attributes={bowling_League_name}

# Relationships
matchups3: BinaryAssociation = BinaryAssociation(
    name="matchups3",
    ends={
        Property(name="bowling_Matchup", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament", type=bowling_Matchup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
games0: BinaryAssociation = BinaryAssociation(
    name="games0",
    ends={
        Property(name="bowling_Game", type=bowling_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Player", type=bowling_Game, multiplicity=Multiplicity(0, 9999))
    }
)
player1: BinaryAssociation = BinaryAssociation(
    name="player1",
    ends={
        Property(name="bowling_Player2", type=bowling_League, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_League", type=bowling_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
games4: BinaryAssociation = BinaryAssociation(
    name="games4",
    ends={
        Property(name="Game", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchup", type=bowling_Game, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
matchup5: BinaryAssociation = BinaryAssociation(
    name="matchup5",
    ends={
        Property(name="Matchup", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games", type=bowling_Matchup, multiplicity=Multiplicity(0, 1))
    }
)
player6: BinaryAssociation = BinaryAssociation(
    name="player6",
    ends={
        Property(name="bowling_Player8", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Game7", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowling",
    types={bowling_Tournament, bowling_Matchup, bowling_Player, bowling_Game, bowling_League, TournamentType},
    associations={matchups3, games0, player1, games4, matchup5, player6},
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