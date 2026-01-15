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
HowOut: Enumeration = Enumeration(
    name="HowOut",
    literals={
            EnumerationLiteral(name="Bowled"),
			EnumerationLiteral(name="Caught"),
			EnumerationLiteral(name="Lbw"),
			EnumerationLiteral(name="Run_Out"),
			EnumerationLiteral(name="Stumped")
    }
)

BallType: Enumeration = Enumeration(
    name="BallType",
    literals={
            EnumerationLiteral(name="three_runs"),
			EnumerationLiteral(name="four_runs"),
			EnumerationLiteral(name="six_runs"),
			EnumerationLiteral(name="dot_ball"),
			EnumerationLiteral(name="one_run"),
			EnumerationLiteral(name="two_runs")
    }
)

ExtraType: Enumeration = Enumeration(
    name="ExtraType",
    literals={
            EnumerationLiteral(name="Wide"),
			EnumerationLiteral(name="NoBall"),
			EnumerationLiteral(name="Bye"),
			EnumerationLiteral(name="LegBye")
    }
)

# Classes
model_Team = Class(name="model::Team")
model_Over = Class(name="model::Over")
model_Player = Class(name="model::Player")
model_Ball = Class(name="model::Ball")
model_Game = Class(name="model::Game")
model_Innings = Class(name="model::Innings")
model_WicketBall = Class(name="model::WicketBall")
Ball = Class(name="Ball")
model_ExtraBall = Class(name="model::ExtraBall")

# model_Team class attributes and methods
model_Team_name: Property = Property(name="name", type=StringType)
model_Team.attributes={model_Team_name}

# model_Over class attributes and methods
model_Over_runs: Property = Property(name="runs", type=IntegerType)
model_Over_BALLS_IN_OVER: Property = Property(name="BALLS_IN_OVER", type=IntegerType)
model_Over_validBalls: Property = Property(name="validBalls", type=IntegerType)
model_Over_isComplete: Property = Property(name="isComplete", type=BooleanType)
model_Over.attributes={model_Over_validBalls, model_Over_isComplete, model_Over_runs, model_Over_BALLS_IN_OVER}

# model_Player class attributes and methods
model_Player_name: Property = Property(name="name", type=StringType)
model_Player_runsScored: Property = Property(name="runsScored", type=IntegerType)
model_Player_noOversBowled: Property = Property(name="noOversBowled", type=StringType)
model_Player_noBallsFaced: Property = Property(name="noBallsFaced", type=IntegerType)
model_Player_howOut: Property = Property(name="howOut", type=StringType)
model_Player.attributes={model_Player_howOut, model_Player_name, model_Player_runsScored, model_Player_noBallsFaced, model_Player_noOversBowled}

# model_Ball class attributes and methods
model_Ball_runs: Property = Property(name="runs", type=StringType)
model_Ball_runValue: Property = Property(name="runValue", type=IntegerType)
model_Ball_switchEnds: Property = Property(name="switchEnds", type=StringType)
model_Ball.attributes={model_Ball_runValue, model_Ball_runs, model_Ball_switchEnds}

# model_Game class attributes and methods
model_Game_date: Property = Property(name="date", type=DateType)
model_Game_venue: Property = Property(name="venue", type=StringType)
model_Game.attributes={model_Game_venue, model_Game_date}

# model_Innings class attributes and methods
model_Innings_noOvers: Property = Property(name="noOvers", type=IntegerType)
model_Innings_total: Property = Property(name="total", type=IntegerType)
model_Innings_wicketsDown: Property = Property(name="wicketsDown", type=IntegerType)
model_Innings_overCount: Property = Property(name="overCount", type=StringType)
model_Innings_Summary: Property = Property(name="Summary", type=StringType)
model_Innings_m_bowlBall: Method = Method(name="bowlBall", parameters={})
model_Innings_m_newOver: Method = Method(name="newOver", parameters={Parameter(name='bowler')}, type=StringType)
model_Innings.attributes={model_Innings_wicketsDown, model_Innings_Summary, model_Innings_total, model_Innings_noOvers, model_Innings_overCount}
model_Innings.methods={model_Innings_m_bowlBall, model_Innings_m_newOver}

# model_WicketBall class attributes and methods
model_WicketBall_howOut: Property = Property(name="howOut", type=StringType)
model_WicketBall.attributes={model_WicketBall_howOut}

# Ball class attributes and methods

# model_ExtraBall class attributes and methods
model_ExtraBall_extraType: Property = Property(name="extraType", type=StringType)
model_ExtraBall_isValidBall: Property = Property(name="isValidBall", type=StringType)
model_ExtraBall.attributes={model_ExtraBall_isValidBall, model_ExtraBall_extraType}

# Relationships
team1: BinaryAssociation = BinaryAssociation(
    name="team1",
    ends={
        Property(name="model_Team", type=model_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Game2", type=model_Team, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
overs3: BinaryAssociation = BinaryAssociation(
    name="overs3",
    ends={
        Property(name="Over", type=model_Innings, multiplicity=Multiplicity(1, 1)),
        Property(name="innings", type=model_Over, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
battingSide4: BinaryAssociation = BinaryAssociation(
    name="battingSide4",
    ends={
        Property(name="model_Team6", type=model_Innings, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Innings5", type=model_Team, multiplicity=Multiplicity(1, 1))
    }
)
bowlingSide7: BinaryAssociation = BinaryAssociation(
    name="bowlingSide7",
    ends={
        Property(name="model_Team9", type=model_Innings, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Innings8", type=model_Team, multiplicity=Multiplicity(1, 1))
    }
)
facingBat10: BinaryAssociation = BinaryAssociation(
    name="facingBat10",
    ends={
        Property(name="model_Player", type=model_Innings, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Innings11", type=model_Player, multiplicity=Multiplicity(1, 1))
    }
)
nonFacingBat12: BinaryAssociation = BinaryAssociation(
    name="nonFacingBat12",
    ends={
        Property(name="model_Player14", type=model_Innings, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Innings13", type=model_Player, multiplicity=Multiplicity(1, 1))
    }
)
balls15: BinaryAssociation = BinaryAssociation(
    name="balls15",
    ends={
        Property(name="model_Ball", type=model_Over, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Over", type=model_Ball, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innings0: BinaryAssociation = BinaryAssociation(
    name="innings0",
    ends={
        Property(name="model_Innings", type=model_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Game", type=model_Innings, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ballsFaced20: BinaryAssociation = BinaryAssociation(
    name="ballsFaced20",
    ends={
        Property(name="Ball", type=model_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="batsman", type=model_Ball, multiplicity=Multiplicity(0, 9999))
    }
)
oversBowled21: BinaryAssociation = BinaryAssociation(
    name="oversBowled21",
    ends={
        Property(name="Over22", type=model_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="bowler", type=model_Over, multiplicity=Multiplicity(0, 9999))
    }
)
wicketball23: BinaryAssociation = BinaryAssociation(
    name="wicketball23",
    ends={
        Property(name="WicketBall", type=model_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="playerOut", type=model_WicketBall, multiplicity=Multiplicity(0, 1))
    }
)
players24: BinaryAssociation = BinaryAssociation(
    name="players24",
    ends={
        Property(name="model_Player26", type=model_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Team25", type=model_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assists27: BinaryAssociation = BinaryAssociation(
    name="assists27",
    ends={
        Property(name="model_Player28", type=model_WicketBall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_WicketBall", type=model_Player, multiplicity=Multiplicity(1, 1))
    }
)
playerOut29: BinaryAssociation = BinaryAssociation(
    name="playerOut29",
    ends={
        Property(name="Player30", type=model_WicketBall, multiplicity=Multiplicity(1, 1)),
        Property(name="wicketball", type=model_Player, multiplicity=Multiplicity(1, 1))
    }
)
innings16: BinaryAssociation = BinaryAssociation(
    name="innings16",
    ends={
        Property(name="Innings", type=model_Over, multiplicity=Multiplicity(1, 1)),
        Property(name="overs", type=model_Innings, multiplicity=Multiplicity(1, 1))
    }
)
bowler17: BinaryAssociation = BinaryAssociation(
    name="bowler17",
    ends={
        Property(name="Player", type=model_Over, multiplicity=Multiplicity(1, 1)),
        Property(name="oversBowled", type=model_Player, multiplicity=Multiplicity(1, 1))
    }
)
batsman18: BinaryAssociation = BinaryAssociation(
    name="batsman18",
    ends={
        Property(name="Player19", type=model_Ball, multiplicity=Multiplicity(1, 1)),
        Property(name="ballsFaced", type=model_Player, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_WicketBall_Ball = Generalization(general=Ball, specific=model_WicketBall)
gen_model_ExtraBall_Ball = Generalization(general=Ball, specific=model_ExtraBall)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Team, model_Over, model_Player, model_Ball, model_Game, model_Innings, model_WicketBall, Ball, model_ExtraBall, HowOut, BallType, ExtraType},
    associations={team1, overs3, battingSide4, bowlingSide7, facingBat10, nonFacingBat12, balls15, innings0, ballsFaced20, oversBowled21, wicketball23, players24, assists27, playerOut29, innings16, bowler17, batsman18},
    generalizations={gen_model_WicketBall_Ball, gen_model_ExtraBall_Ball},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)