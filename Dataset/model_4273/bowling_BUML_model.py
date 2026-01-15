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

Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="Female"),
			EnumerationLiteral(name="Male")
    }
)

# Classes
bowling_League = Class(name="bowling::League")
bowling_Player = Class(name="bowling::Player")
bowling_Tournament = Class(name="bowling::Tournament")
bowling_Matchup = Class(name="bowling::Matchup")
bowling_PlayerToPointsMap = Class(name="bowling::PlayerToPointsMap")
bowling_RefereeToGamesMap = Class(name="bowling::RefereeToGamesMap")
bowling_Game = Class(name="bowling::Game")
bowling_Referee = Class(name="bowling::Referee")
bowling_Area = Class(name="bowling::Area")
bowling_Fan = Class(name="bowling::Fan")
bowling_Merchandise = Class(name="bowling::Merchandise")

# bowling_League class attributes and methods
bowling_League_name: Property = Property(name="name", type=StringType)
bowling_League.attributes={bowling_League_name}

# bowling_Player class attributes and methods
bowling_Player_name: Property = Property(name="name", type=StringType)
bowling_Player_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowling_Player_height: Property = Property(name="height", type=FloatType)
bowling_Player_isProfessional: Property = Property(name="isProfessional", type=BooleanType)
bowling_Player_eMails: Property = Property(name="eMails", type=StringType)
bowling_Player_numberOfVictories: Property = Property(name="numberOfVictories", type=IntegerType)
bowling_Player_playedTournamentTypes: Property = Property(name="playedTournamentTypes", type=StringType)
bowling_Player_winLossRatio: Property = Property(name="winLossRatio", type=StringType)
bowling_Player_gender: Property = Property(name="gender", type=StringType)
bowling_Player_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='chain')}, type=BooleanType)
bowling_Player.attributes={bowling_Player_name, bowling_Player_eMails, bowling_Player_dateOfBirth, bowling_Player_isProfessional, bowling_Player_height, bowling_Player_playedTournamentTypes, bowling_Player_gender, bowling_Player_winLossRatio, bowling_Player_numberOfVictories}
bowling_Player.methods={bowling_Player_m_validate}

# bowling_Tournament class attributes and methods
bowling_Tournament_type: Property = Property(name="type", type=StringType)
bowling_Tournament_priceMoney: Property = Property(name="priceMoney", type=FloatType)
bowling_Tournament_receivesTrophy: Property = Property(name="receivesTrophy", type=BooleanType)
bowling_Tournament_matchDays: Property = Property(name="matchDays", type=DateType)
bowling_Tournament.attributes={bowling_Tournament_type, bowling_Tournament_receivesTrophy, bowling_Tournament_matchDays, bowling_Tournament_priceMoney}

# bowling_Matchup class attributes and methods
bowling_Matchup_nrSpectators: Property = Property(name="nrSpectators", type=StringType)
bowling_Matchup.attributes={bowling_Matchup_nrSpectators}

# bowling_PlayerToPointsMap class attributes and methods
bowling_PlayerToPointsMap_value: Property = Property(name="value", type=StringType)
bowling_PlayerToPointsMap.attributes={bowling_PlayerToPointsMap_value}

# bowling_RefereeToGamesMap class attributes and methods

# bowling_Game class attributes and methods
bowling_Game_frames: Property = Property(name="frames", type=IntegerType)
bowling_Game.attributes={bowling_Game_frames}

# bowling_Referee class attributes and methods
bowling_Referee_dateOfBirth: Property = Property(name="dateOfBirth", type=StringType)
bowling_Referee.attributes={bowling_Referee_dateOfBirth}

# bowling_Area class attributes and methods

# bowling_Fan class attributes and methods
bowling_Fan_name: Property = Property(name="name", type=StringType)
bowling_Fan_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowling_Fan_hasSeasonTicket: Property = Property(name="hasSeasonTicket", type=BooleanType)
bowling_Fan_eMails: Property = Property(name="eMails", type=StringType)
bowling_Fan_gender: Property = Property(name="gender", type=StringType)
bowling_Fan_numberOfTournamentsVisited: Property = Property(name="numberOfTournamentsVisited", type=IntegerType)
bowling_Fan_moneySpentOnTickets: Property = Property(name="moneySpentOnTickets", type=FloatType)
bowling_Fan.attributes={bowling_Fan_hasSeasonTicket, bowling_Fan_moneySpentOnTickets, bowling_Fan_gender, bowling_Fan_eMails, bowling_Fan_name, bowling_Fan_numberOfTournamentsVisited, bowling_Fan_dateOfBirth}

# bowling_Merchandise class attributes and methods
bowling_Merchandise_name: Property = Property(name="name", type=StringType)
bowling_Merchandise_price: Property = Property(name="price", type=StringType)
bowling_Merchandise_serialNumber: Property = Property(name="serialNumber", type=StringType)
bowling_Merchandise.attributes={bowling_Merchandise_price, bowling_Merchandise_name, bowling_Merchandise_serialNumber}

# Relationships
areas25: BinaryAssociation = BinaryAssociation(
    name="areas25",
    ends={
        Property(name="bowling_Area", type=bowling_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Area24", type=bowling_Area, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tournaments26: BinaryAssociation = BinaryAssociation(
    name="tournaments26",
    ends={
        Property(name="bowling_Tournament28", type=bowling_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Area27", type=bowling_Tournament, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
playerPoints2: BinaryAssociation = BinaryAssociation(
    name="playerPoints2",
    ends={
        Property(name="bowling_PlayerToPointsMap", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament3", type=bowling_PlayerToPointsMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
players4: BinaryAssociation = BinaryAssociation(
    name="players4",
    ends={
        Property(name="bowling_Player6", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament5", type=bowling_Player, multiplicity=Multiplicity(0, 9999))
    }
)
referees7: BinaryAssociation = BinaryAssociation(
    name="referees7",
    ends={
        Property(name="bowling_RefereeToGamesMap", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament8", type=bowling_RefereeToGamesMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
games9: BinaryAssociation = BinaryAssociation(
    name="games9",
    ends={
        Property(name="Game", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchup", type=bowling_Game, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
matchup10: BinaryAssociation = BinaryAssociation(
    name="matchup10",
    ends={
        Property(name="Matchup", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games", type=bowling_Matchup, multiplicity=Multiplicity(1, 1))
    }
)
player11: BinaryAssociation = BinaryAssociation(
    name="player11",
    ends={
        Property(name="bowling_Player12", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Game", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)
key13: BinaryAssociation = BinaryAssociation(
    name="key13",
    ends={
        Property(name="bowling_Player15", type=bowling_PlayerToPointsMap, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_PlayerToPointsMap14", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)
league16: BinaryAssociation = BinaryAssociation(
    name="league16",
    ends={
        Property(name="bowling_League17", type=bowling_Referee, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Referee", type=bowling_League, multiplicity=Multiplicity(0, 1))
    }
)
key18: BinaryAssociation = BinaryAssociation(
    name="key18",
    ends={
        Property(name="bowling_Referee20", type=bowling_RefereeToGamesMap, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_RefereeToGamesMap19", type=bowling_Referee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="bowling_Game23", type=bowling_RefereeToGamesMap, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_RefereeToGamesMap22", type=bowling_Game, multiplicity=Multiplicity(0, 1))
    }
)
favouritePlayer29: BinaryAssociation = BinaryAssociation(
    name="favouritePlayer29",
    ends={
        Property(name="bowling_Player30", type=bowling_Fan, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Fan", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)
fanMerchandise31: BinaryAssociation = BinaryAssociation(
    name="fanMerchandise31",
    ends={
        Property(name="bowling_Merchandise", type=bowling_Fan, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Fan32", type=bowling_Merchandise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
favouriteMerchandise33: BinaryAssociation = BinaryAssociation(
    name="favouriteMerchandise33",
    ends={
        Property(name="bowling_Merchandise35", type=bowling_Fan, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Fan34", type=bowling_Merchandise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visitedTournaments36: BinaryAssociation = BinaryAssociation(
    name="visitedTournaments36",
    ends={
        Property(name="bowling_Tournament38", type=bowling_Fan, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Fan37", type=bowling_Tournament, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowling",
    types={bowling_League, bowling_Player, bowling_Tournament, bowling_Matchup, bowling_PlayerToPointsMap, bowling_RefereeToGamesMap, bowling_Game, bowling_Referee, bowling_Area, bowling_Fan, bowling_Merchandise, TournamentType, Gender},
    associations={areas25, tournaments26, players0, matchups1, playerPoints2, players4, referees7, games9, matchup10, player11, key13, league16, key18, value21, favouritePlayer29, fanMerchandise31, favouriteMerchandise33, visitedTournaments36},
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