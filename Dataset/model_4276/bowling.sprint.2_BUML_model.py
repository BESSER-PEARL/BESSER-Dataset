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
bowling_Alley = Class(name="bowling::Alley")
bowling_Lane = Class(name="bowling::Lane")
bowling_Game = Class(name="bowling::Game")

# bowling_Player class attributes and methods
bowling_Player_name: Property = Property(name="name", type=StringType)
bowling_Player_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowling_Player_height: Property = Property(name="height", type=FloatType)
bowling_Player_isProfessional: Property = Property(name="isProfessional", type=BooleanType)
bowling_Player.attributes={bowling_Player_height, bowling_Player_name, bowling_Player_isProfessional, bowling_Player_dateOfBirth}

# bowling_League class attributes and methods
bowling_League_name: Property = Property(name="name", type=StringType)
bowling_League.attributes={bowling_League_name}

# bowling_Tournament class attributes and methods
bowling_Tournament_name: Property = Property(name="name", type=StringType)
bowling_Tournament_type: Property = Property(name="type", type=StringType)
bowling_Tournament.attributes={bowling_Tournament_name, bowling_Tournament_type}

# bowling_Matchup class attributes and methods
bowling_Matchup_name: Property = Property(name="name", type=StringType)
bowling_Matchup.attributes={bowling_Matchup_name}

# bowling_Alley class attributes and methods
bowling_Alley_name: Property = Property(name="name", type=StringType)
bowling_Alley.attributes={bowling_Alley_name}

# bowling_Lane class attributes and methods
bowling_Lane_number: Property = Property(name="number", type=IntegerType)
bowling_Lane.attributes={bowling_Lane_number}

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
        Property(name="bowling_Game", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Matchup3", type=bowling_Game, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
player4: BinaryAssociation = BinaryAssociation(
    name="player4",
    ends={
        Property(name="bowling_Player6", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Game5", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)
leagues7: BinaryAssociation = BinaryAssociation(
    name="leagues7",
    ends={
        Property(name="bowling_League8", type=bowling_Alley, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Alley", type=bowling_League, multiplicity=Multiplicity(0, 9999))
    }
)
tournaments9: BinaryAssociation = BinaryAssociation(
    name="tournaments9",
    ends={
        Property(name="bowling_Tournament11", type=bowling_Alley, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Alley10", type=bowling_Tournament, multiplicity=Multiplicity(0, 9999))
    }
)
lanes12: BinaryAssociation = BinaryAssociation(
    name="lanes12",
    ends={
        Property(name="bowling_Lane", type=bowling_Alley, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Alley13", type=bowling_Lane, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowling",
    types={bowling_Player, bowling_League, bowling_Tournament, bowling_Matchup, bowling_Alley, bowling_Lane, bowling_Game, TournamentType},
    associations={players0, matchups1, games2, player4, leagues7, tournaments9, lanes12},
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