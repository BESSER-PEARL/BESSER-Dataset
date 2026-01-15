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
bowling_Player_height: Property = Property(name="height", type=FloatType)
bowling_Player_isProfessional: Property = Property(name="isProfessional", type=BooleanType)
bowling_Player.attributes={bowling_Player_isProfessional, bowling_Player_dateOfBirth, bowling_Player_name, bowling_Player_height}

# bowling_League class attributes and methods
bowling_League_name: Property = Property(name="name", type=StringType)
bowling_League.attributes={bowling_League_name}

# bowling_Tournament class attributes and methods
bowling_Tournament_type: Property = Property(name="type", type=StringType)
bowling_Tournament.attributes={bowling_Tournament_type}

# bowling_Matchup class attributes and methods

# bowling_Game class attributes and methods
bowling_Game_frames: Property = Property(name="frames", type=IntegerType)
bowling_Game.attributes={bowling_Game_frames}

# Relationships
players0: BinaryAssociation = BinaryAssociation(
    name="players0",
    ends={
        Property(name="bowling_Player", type=bowling_League, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_League", type=bowling_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subleagues2: BinaryAssociation = BinaryAssociation(
    name="subleagues2",
    ends={
        Property(name="bowling_League3", type=bowling_League, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_League1", type=bowling_League, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tournaments4: BinaryAssociation = BinaryAssociation(
    name="tournaments4",
    ends={
        Property(name="bowling_Tournament", type=bowling_League, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_League5", type=bowling_Tournament, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matchups6: BinaryAssociation = BinaryAssociation(
    name="matchups6",
    ends={
        Property(name="bowling_Matchup", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament7", type=bowling_Matchup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
games8: BinaryAssociation = BinaryAssociation(
    name="games8",
    ends={
        Property(name="Game", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchup", type=bowling_Game, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
matchup9: BinaryAssociation = BinaryAssociation(
    name="matchup9",
    ends={
        Property(name="Matchup", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games", type=bowling_Matchup, multiplicity=Multiplicity(1, 1))
    }
)
player10: BinaryAssociation = BinaryAssociation(
    name="player10",
    ends={
        Property(name="bowling_Player11", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Game", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowling",
    types={bowling_Player, bowling_League, bowling_Tournament, bowling_Matchup, bowling_Game, TournamentType},
    associations={players0, subleagues2, tournaments4, matchups6, games8, matchup9, player10},
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