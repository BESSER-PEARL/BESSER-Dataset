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
bowling_Player = Class(name="bowling::Player")
bowling_League = Class(name="bowling::League")
bowling_Tournament = Class(name="bowling::Tournament")
bowling_Matchup = Class(name="bowling::Matchup")
bowling_Game = Class(name="bowling::Game")

# bowling_Player class attributes and methods
bowling_Player_name: Property = Property(name="name", type=StringType)
bowling_Player_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowling_Player.attributes={bowling_Player_dateOfBirth, bowling_Player_name}

# bowling_League class attributes and methods
bowling_League_name: Property = Property(name="name", type=StringType)
bowling_League.attributes={bowling_League_name}

# bowling_Tournament class attributes and methods
bowling_Tournament_type: Property = Property(name="type", type=StringType)
bowling_Tournament.attributes={bowling_Tournament_type}

# bowling_Matchup class attributes and methods

# bowling_Game class attributes and methods

# Relationships
players0: BinaryAssociation = BinaryAssociation(
    name="players0",
    ends={
        Property(name="bowling_Player", type=bowling_League, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_League", type=bowling_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matchups1: BinaryAssociation = BinaryAssociation(
    name="matchups1",
    ends={
        Property(name="bowling_Matchup", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament", type=bowling_Matchup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
games2: BinaryAssociation = BinaryAssociation(
    name="games2",
    ends={
        Property(name="Game", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchup", type=bowling_Game, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
matchup3: BinaryAssociation = BinaryAssociation(
    name="matchup3",
    ends={
        Property(name="Matchup", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games", type=bowling_Matchup, multiplicity=Multiplicity(0, 1))
    }
)
player4: BinaryAssociation = BinaryAssociation(
    name="player4",
    ends={
        Property(name="bowling_Player5", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Game", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowling",
    types={bowling_Player, bowling_League, bowling_Tournament, bowling_Matchup, bowling_Game, TournamentType},
    associations={players0, matchups1, games2, matchup3, player4},
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