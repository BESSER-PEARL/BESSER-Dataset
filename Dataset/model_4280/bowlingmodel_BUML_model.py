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
            EnumerationLiteral(name="Amateur"),
			EnumerationLiteral(name="Pro")
    }
)

# Classes
bowling_Game = Class(name="bowling::Game")
bowling_Playerlist = Class(name="bowling::Playerlist")
bowling_Player = Class(name="bowling::Player")
bowling_Matchup = Class(name="bowling::Matchup")
bowling_Tournament = Class(name="bowling::Tournament")

# bowling_Game class attributes and methods
bowling_Game_date: Property = Property(name="date", type=DateType)
bowling_Game_frames: Property = Property(name="frames", type=IntegerType)
bowling_Game.attributes={bowling_Game_frames, bowling_Game_date}

# bowling_Playerlist class attributes and methods
bowling_Playerlist_name: Property = Property(name="name", type=StringType)
bowling_Playerlist.attributes={bowling_Playerlist_name}

# bowling_Player class attributes and methods
bowling_Player_streetnumber: Property = Property(name="streetnumber", type=IntegerType)
bowling_Player_city: Property = Property(name="city", type=StringType)
bowling_Player_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowling_Player_height: Property = Property(name="height", type=FloatType)
bowling_Player_isProfessional: Property = Property(name="isProfessional", type=BooleanType)
bowling_Player_firstname: Property = Property(name="firstname", type=StringType)
bowling_Player_lastname: Property = Property(name="lastname", type=StringType)
bowling_Player_street: Property = Property(name="street", type=StringType)
bowling_Player.attributes={bowling_Player_lastname, bowling_Player_firstname, bowling_Player_height, bowling_Player_isProfessional, bowling_Player_street, bowling_Player_city, bowling_Player_dateOfBirth, bowling_Player_streetnumber}

# bowling_Matchup class attributes and methods

# bowling_Tournament class attributes and methods
bowling_Tournament_title: Property = Property(name="title", type=StringType)
bowling_Tournament_type: Property = Property(name="type", type=StringType)
bowling_Tournament.attributes={bowling_Tournament_title, bowling_Tournament_type}

# Relationships
game0: BinaryAssociation = BinaryAssociation(
    name="game0",
    ends={
        Property(name="Game", type=bowling_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="player", type=bowling_Game, multiplicity=Multiplicity(0, 9999))
    }
)
playerlist1: BinaryAssociation = BinaryAssociation(
    name="playerlist1",
    ends={
        Property(name="Playerlist", type=bowling_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="player2", type=bowling_Playerlist, multiplicity=Multiplicity(0, 1))
    }
)
playerlist16: BinaryAssociation = BinaryAssociation(
    name="playerlist16",
    ends={
        Property(name="Playerlist18", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournament17", type=bowling_Playerlist, multiplicity=Multiplicity(0, 1))
    }
)
player3: BinaryAssociation = BinaryAssociation(
    name="player3",
    ends={
        Property(name="Player", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)
matchup4: BinaryAssociation = BinaryAssociation(
    name="matchup4",
    ends={
        Property(name="Matchup", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game5", type=bowling_Matchup, multiplicity=Multiplicity(0, 1))
    }
)
game6: BinaryAssociation = BinaryAssociation(
    name="game6",
    ends={
        Property(name="Game7", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchup", type=bowling_Game, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
tournament8: BinaryAssociation = BinaryAssociation(
    name="tournament8",
    ends={
        Property(name="Tournament", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchups", type=bowling_Tournament, multiplicity=Multiplicity(0, 1))
    }
)
player9: BinaryAssociation = BinaryAssociation(
    name="player9",
    ends={
        Property(name="Player10", type=bowling_Playerlist, multiplicity=Multiplicity(1, 1)),
        Property(name="playerlist", type=bowling_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tournament11: BinaryAssociation = BinaryAssociation(
    name="tournament11",
    ends={
        Property(name="Tournament13", type=bowling_Playerlist, multiplicity=Multiplicity(1, 1)),
        Property(name="playerlist12", type=bowling_Tournament, multiplicity=Multiplicity(0, 1))
    }
)
matchups14: BinaryAssociation = BinaryAssociation(
    name="matchups14",
    ends={
        Property(name="Matchup15", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournament", type=bowling_Matchup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowling",
    types={bowling_Game, bowling_Playerlist, bowling_Player, bowling_Matchup, bowling_Tournament, TournamentType},
    associations={game0, playerlist1, playerlist16, player3, matchup4, game6, tournament8, player9, tournament11, matchups14},
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