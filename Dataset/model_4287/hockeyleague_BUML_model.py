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
DefencePositionKind: Enumeration = Enumeration(
    name="DefencePositionKind",
    literals={
            EnumerationLiteral(name="left_defence"),
			EnumerationLiteral(name="right_defence")
    }
)

ForwardPositionKind: Enumeration = Enumeration(
    name="ForwardPositionKind",
    literals={
            EnumerationLiteral(name="left_wing"),
			EnumerationLiteral(name="right_wing"),
			EnumerationLiteral(name="center")
    }
)

HeightKind: Enumeration = Enumeration(
    name="HeightKind",
    literals={
            EnumerationLiteral(name="inches"),
			EnumerationLiteral(name="centimeters")
    }
)

ShotKind: Enumeration = Enumeration(
    name="ShotKind",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
    }
)

WeightKind: Enumeration = Enumeration(
    name="WeightKind",
    literals={
            EnumerationLiteral(name="pounds"),
			EnumerationLiteral(name="kilograms")
    }
)

# Classes
HockeyleagueObject = Class(name="HockeyleagueObject")
hockeyleague_Defence = Class(name="hockeyleague::Defence")
Player = Class(name="Player")
hockeyleague_PlayerStats = Class(name="hockeyleague::PlayerStats")
hockeyleague_Forward = Class(name="hockeyleague::Forward")
hockeyleague_Goalie = Class(name="hockeyleague::Goalie")
hockeyleague_GoalieStats = Class(name="hockeyleague::GoalieStats")
hockeyleague_Team = Class(name="hockeyleague::Team")
hockeyleague_Arena = Class(name="hockeyleague::Arena")
hockeyleague_HockeyleagueObject = Class(name="hockeyleague::HockeyleagueObject", is_abstract=True)
hockeyleague_League = Class(name="hockeyleague::League")
hockeyleague_Player = Class(name="hockeyleague::Player", is_abstract=True)

# HockeyleagueObject class attributes and methods

# hockeyleague_Defence class attributes and methods
hockeyleague_Defence_position: Property = Property(name="position", type=StringType)
hockeyleague_Defence.attributes={hockeyleague_Defence_position}

# Player class attributes and methods

# hockeyleague_PlayerStats class attributes and methods
hockeyleague_PlayerStats_year: Property = Property(name="year", type=StringType)
hockeyleague_PlayerStats_gamesPlayedIn: Property = Property(name="gamesPlayedIn", type=IntegerType)
hockeyleague_PlayerStats_goals: Property = Property(name="goals", type=IntegerType)
hockeyleague_PlayerStats_assists: Property = Property(name="assists", type=IntegerType)
hockeyleague_PlayerStats_points: Property = Property(name="points", type=IntegerType)
hockeyleague_PlayerStats_plusMinus: Property = Property(name="plusMinus", type=IntegerType)
hockeyleague_PlayerStats_penaltyMinutes: Property = Property(name="penaltyMinutes", type=IntegerType)
hockeyleague_PlayerStats_powerPlayGoals: Property = Property(name="powerPlayGoals", type=IntegerType)
hockeyleague_PlayerStats_shortHandedGoals: Property = Property(name="shortHandedGoals", type=IntegerType)
hockeyleague_PlayerStats_gameWinningGoals: Property = Property(name="gameWinningGoals", type=IntegerType)
hockeyleague_PlayerStats_shots: Property = Property(name="shots", type=IntegerType)
hockeyleague_PlayerStats_shotPercentage: Property = Property(name="shotPercentage", type=FloatType)
hockeyleague_PlayerStats.attributes={hockeyleague_PlayerStats_shots, hockeyleague_PlayerStats_shotPercentage, hockeyleague_PlayerStats_powerPlayGoals, hockeyleague_PlayerStats_year, hockeyleague_PlayerStats_plusMinus, hockeyleague_PlayerStats_assists, hockeyleague_PlayerStats_gamesPlayedIn, hockeyleague_PlayerStats_penaltyMinutes, hockeyleague_PlayerStats_gameWinningGoals, hockeyleague_PlayerStats_shortHandedGoals, hockeyleague_PlayerStats_goals, hockeyleague_PlayerStats_points}

# hockeyleague_Forward class attributes and methods
hockeyleague_Forward_position: Property = Property(name="position", type=StringType)
hockeyleague_Forward.attributes={hockeyleague_Forward_position}

# hockeyleague_Goalie class attributes and methods

# hockeyleague_GoalieStats class attributes and methods
hockeyleague_GoalieStats_year: Property = Property(name="year", type=StringType)
hockeyleague_GoalieStats_gamesPlayedIn: Property = Property(name="gamesPlayedIn", type=IntegerType)
hockeyleague_GoalieStats_minutesPlayedIn: Property = Property(name="minutesPlayedIn", type=IntegerType)
hockeyleague_GoalieStats_goalsAgainstAverage: Property = Property(name="goalsAgainstAverage", type=FloatType)
hockeyleague_GoalieStats_wins: Property = Property(name="wins", type=IntegerType)
hockeyleague_GoalieStats_losses: Property = Property(name="losses", type=IntegerType)
hockeyleague_GoalieStats_ties: Property = Property(name="ties", type=IntegerType)
hockeyleague_GoalieStats_emptyNetGoals: Property = Property(name="emptyNetGoals", type=IntegerType)
hockeyleague_GoalieStats_shutouts: Property = Property(name="shutouts", type=IntegerType)
hockeyleague_GoalieStats_goalsAgainst: Property = Property(name="goalsAgainst", type=IntegerType)
hockeyleague_GoalieStats_saves: Property = Property(name="saves", type=IntegerType)
hockeyleague_GoalieStats_penaltyMinutes: Property = Property(name="penaltyMinutes", type=IntegerType)
hockeyleague_GoalieStats_goals: Property = Property(name="goals", type=IntegerType)
hockeyleague_GoalieStats_assists: Property = Property(name="assists", type=IntegerType)
hockeyleague_GoalieStats_points: Property = Property(name="points", type=IntegerType)
hockeyleague_GoalieStats.attributes={hockeyleague_GoalieStats_year, hockeyleague_GoalieStats_wins, hockeyleague_GoalieStats_gamesPlayedIn, hockeyleague_GoalieStats_emptyNetGoals, hockeyleague_GoalieStats_saves, hockeyleague_GoalieStats_penaltyMinutes, hockeyleague_GoalieStats_shutouts, hockeyleague_GoalieStats_goalsAgainst, hockeyleague_GoalieStats_assists, hockeyleague_GoalieStats_points, hockeyleague_GoalieStats_goalsAgainstAverage, hockeyleague_GoalieStats_goals, hockeyleague_GoalieStats_losses, hockeyleague_GoalieStats_ties, hockeyleague_GoalieStats_minutesPlayedIn}

# hockeyleague_Team class attributes and methods

# hockeyleague_Arena class attributes and methods
hockeyleague_Arena_address: Property = Property(name="address", type=StringType)
hockeyleague_Arena_capacity: Property = Property(name="capacity", type=IntegerType)
hockeyleague_Arena.attributes={hockeyleague_Arena_capacity, hockeyleague_Arena_address}

# hockeyleague_HockeyleagueObject class attributes and methods
hockeyleague_HockeyleagueObject_name: Property = Property(name="name", type=StringType)
hockeyleague_HockeyleagueObject.attributes={hockeyleague_HockeyleagueObject_name}

# hockeyleague_League class attributes and methods
hockeyleague_League_headoffice: Property = Property(name="headoffice", type=StringType)
hockeyleague_League.attributes={hockeyleague_League_headoffice}

# hockeyleague_Player class attributes and methods
hockeyleague_Player_shot: Property = Property(name="shot", type=StringType)
hockeyleague_Player_birthdate: Property = Property(name="birthdate", type=StringType)
hockeyleague_Player_birthplace: Property = Property(name="birthplace", type=StringType)
hockeyleague_Player_number: Property = Property(name="number", type=IntegerType)
hockeyleague_Player_heightMesurement: Property = Property(name="heightMesurement", type=StringType)
hockeyleague_Player_heightValue: Property = Property(name="heightValue", type=IntegerType)
hockeyleague_Player_weightMesurement: Property = Property(name="weightMesurement", type=StringType)
hockeyleague_Player_weightValue: Property = Property(name="weightValue", type=IntegerType)
hockeyleague_Player.attributes={hockeyleague_Player_birthdate, hockeyleague_Player_number, hockeyleague_Player_birthplace, hockeyleague_Player_heightValue, hockeyleague_Player_weightValue, hockeyleague_Player_weightMesurement, hockeyleague_Player_shot, hockeyleague_Player_heightMesurement}

# Relationships
playerStats0: BinaryAssociation = BinaryAssociation(
    name="playerStats0",
    ends={
        Property(name="hockeyleague_PlayerStats", type=hockeyleague_Defence, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_Defence", type=hockeyleague_PlayerStats, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
playerStats1: BinaryAssociation = BinaryAssociation(
    name="playerStats1",
    ends={
        Property(name="hockeyleague_PlayerStats2", type=hockeyleague_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_Forward", type=hockeyleague_PlayerStats, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goalieStats3: BinaryAssociation = BinaryAssociation(
    name="goalieStats3",
    ends={
        Property(name="hockeyleague_GoalieStats", type=hockeyleague_Goalie, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_Goalie", type=hockeyleague_GoalieStats, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
team4: BinaryAssociation = BinaryAssociation(
    name="team4",
    ends={
        Property(name="hockeyleague_Team", type=hockeyleague_GoalieStats, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_GoalieStats5", type=hockeyleague_Team, multiplicity=Multiplicity(0, 1))
    }
)
team8: BinaryAssociation = BinaryAssociation(
    name="team8",
    ends={
        Property(name="hockeyleague_Team10", type=hockeyleague_PlayerStats, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_PlayerStats9", type=hockeyleague_Team, multiplicity=Multiplicity(0, 1))
    }
)
forwards11: BinaryAssociation = BinaryAssociation(
    name="forwards11",
    ends={
        Property(name="hockeyleague_Forward13", type=hockeyleague_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_Team12", type=hockeyleague_Forward, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defencemen14: BinaryAssociation = BinaryAssociation(
    name="defencemen14",
    ends={
        Property(name="hockeyleague_Defence16", type=hockeyleague_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_Team15", type=hockeyleague_Defence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goalies17: BinaryAssociation = BinaryAssociation(
    name="goalies17",
    ends={
        Property(name="hockeyleague_Goalie19", type=hockeyleague_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_Team18", type=hockeyleague_Goalie, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arena20: BinaryAssociation = BinaryAssociation(
    name="arena20",
    ends={
        Property(name="hockeyleague_Arena", type=hockeyleague_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_Team21", type=hockeyleague_Arena, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
teams6: BinaryAssociation = BinaryAssociation(
    name="teams6",
    ends={
        Property(name="hockeyleague_Team7", type=hockeyleague_League, multiplicity=Multiplicity(1, 1)),
        Property(name="hockeyleague_League", type=hockeyleague_Team, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_hockeyleague_Arena_HockeyleagueObject = Generalization(general=HockeyleagueObject, specific=hockeyleague_Arena)
gen_hockeyleague_Defence_Player = Generalization(general=Player, specific=hockeyleague_Defence)
gen_hockeyleague_Forward_Player = Generalization(general=Player, specific=hockeyleague_Forward)
gen_hockeyleague_Goalie_Player = Generalization(general=Player, specific=hockeyleague_Goalie)
gen_hockeyleague_Team_HockeyleagueObject = Generalization(general=HockeyleagueObject, specific=hockeyleague_Team)
gen_hockeyleague_League_HockeyleagueObject = Generalization(general=HockeyleagueObject, specific=hockeyleague_League)
gen_hockeyleague_Player_HockeyleagueObject = Generalization(general=HockeyleagueObject, specific=hockeyleague_Player)

# Domain Model
domain_model = DomainModel(
    name="hockeyleague",
    types={HockeyleagueObject, hockeyleague_Defence, Player, hockeyleague_PlayerStats, hockeyleague_Forward, hockeyleague_Goalie, hockeyleague_GoalieStats, hockeyleague_Team, hockeyleague_Arena, hockeyleague_HockeyleagueObject, hockeyleague_League, hockeyleague_Player, DefencePositionKind, ForwardPositionKind, HeightKind, ShotKind, WeightKind},
    associations={playerStats0, playerStats1, goalieStats3, team4, team8, forwards11, defencemen14, goalies17, arena20, teams6},
    generalizations={gen_hockeyleague_Arena_HockeyleagueObject, gen_hockeyleague_Defence_Player, gen_hockeyleague_Forward_Player, gen_hockeyleague_Goalie_Player, gen_hockeyleague_Team_HockeyleagueObject, gen_hockeyleague_League_HockeyleagueObject, gen_hockeyleague_Player_HockeyleagueObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)