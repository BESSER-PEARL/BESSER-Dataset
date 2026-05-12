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

# Classes
Yahtzee_Game = Class(name="Yahtzee_Game")
Yahtzee_Turn = Class(name="Yahtzee_Turn")
Yahtzee_Scoring = Class(name="Yahtzee_Scoring")
Yahtzee_Display = Class(name="Yahtzee_Display")
Yahtzee_Players = Class(name="Yahtzee_Players")
Class_ = Class(name="Class")
Class1 = Class(name="Class1")
Scoring = Class(name="Scoring")
Turn = Class(name="Turn")
Players = Class(name="Players")
Yahtzee_Component = Class(name="Yahtzee_Component")
Player_Actor = Class(name="Player_Actor")
Yahtzee_Display1 = Class(name="Yahtzee_Display1")
Yahtzee_Turn1 = Class(name="Yahtzee_Turn1")
Yahtzee_Scoring1 = Class(name="Yahtzee_Scoring1")
Yahtzee_Players1 = Class(name="Yahtzee_Players1")
Display = Class(name="Display")
Get_Player_Name_external = Class(name="Get_Player_Name_external")
Get_Instructions_external = Class(name="Get_Instructions_external")
Roll_First_external = Class(name="Roll_First_external")
Game_Start_external = Class(name="Game_Start_external")
Computer_Turn_external = Class(name="Computer_Turn_external")
Roll_Dice_external = Class(name="Roll_Dice_external")
Score_Roll_external = Class(name="Score_Roll_external")
Next_Turn_external = Class(name="Next_Turn_external")
Announce_Winner_external = Class(name="Announce_Winner_external")
Play_Again_external = Class(name="Play_Again_external")

# Yahtzee_Game class attributes and methods
Yahtzee_Game_Player: Property = Property(name="Player", type=Class_)
Yahtzee_Game_CompPlayer: Property = Property(name="CompPlayer", type=Class1)
Yahtzee_Game_First: Property = Property(name="First", type=IntegerType)
Yahtzee_Game_Again: Property = Property(name="Again", type=BooleanType)
Yahtzee_Game.attributes={Yahtzee_Game_Again, Yahtzee_Game_CompPlayer, Yahtzee_Game_Player, Yahtzee_Game_First}

# Yahtzee_Turn class attributes and methods

# Yahtzee_Scoring class attributes and methods

# Yahtzee_Display class attributes and methods
Yahtzee_Display_PanelScorecard: Property = Property(name="PanelScorecard", type=StringType)
Yahtzee_Display_PanelChoices: Property = Property(name="PanelChoices", type=StringType)
Yahtzee_Display_PanelPrimary: Property = Property(name="PanelPrimary", type=StringType)
Yahtzee_Display_PanelGameName: Property = Property(name="PanelGameName", type=StringType)
Yahtzee_Display_PanelNames: Property = Property(name="PanelNames", type=StringType)
Yahtzee_Display.attributes={Yahtzee_Display_PanelChoices, Yahtzee_Display_PanelGameName, Yahtzee_Display_PanelNames, Yahtzee_Display_PanelScorecard, Yahtzee_Display_PanelPrimary}

# Yahtzee_Players class attributes and methods
Yahtzee_Players_Name: Property = Property(name="Name", type=StringType)
Yahtzee_Players_Score: Property = Property(name="Score", type=StringType)
Yahtzee_Players.attributes={Yahtzee_Players_Name, Yahtzee_Players_Score}

# Class class attributes and methods

# Class1 class attributes and methods

# Scoring class attributes and methods

# Turn class attributes and methods

# Players class attributes and methods

# Yahtzee_Component class attributes and methods

# Player_Actor class attributes and methods

# Yahtzee_Display1 class attributes and methods
Yahtzee_Display1_Player: Property = Property(name="Player", type=Yahtzee_Players)
Yahtzee_Display1_Computer: Property = Property(name="Computer", type=Yahtzee_Players)
Yahtzee_Display1_Jpanel: Property = Property(name="Jpanel", type=Yahtzee_Display)
Yahtzee_Display1_JFrame: Property = Property(name="JFrame", type=Yahtzee_Display)
Yahtzee_Display1_Jlabel: Property = Property(name="Jlabel", type=Yahtzee_Display)
Yahtzee_Display1_JRadioButton: Property = Property(name="JRadioButton", type=Yahtzee_Display)
Yahtzee_Display1_JButton: Property = Property(name="JButton", type=Yahtzee_Display)
Yahtzee_Display1_JTextField: Property = Property(name="JTextField", type=Yahtzee_Display)
Yahtzee_Display1_JScrollPanel: Property = Property(name="JScrollPanel", type=Yahtzee_Display1)
Yahtzee_Display1_JImageIcon: Property = Property(name="JImageIcon", type=Yahtzee_Display)
Yahtzee_Display1_Temp: Property = Property(name="Temp", type=IntegerType)
Yahtzee_Display1_Temp1: Property = Property(name="Temp1", type=IntegerType)
Yahtzee_Display1.attributes={Yahtzee_Display1_Player, Yahtzee_Display1_JScrollPanel, Yahtzee_Display1_JTextField, Yahtzee_Display1_JButton, Yahtzee_Display1_JImageIcon, Yahtzee_Display1_JFrame, Yahtzee_Display1_JRadioButton, Yahtzee_Display1_Temp, Yahtzee_Display1_Jlabel, Yahtzee_Display1_Computer, Yahtzee_Display1_Temp1, Yahtzee_Display1_Jpanel}

# Yahtzee_Turn1 class attributes and methods
Yahtzee_Turn1_Dice: Property = Property(name="Dice", type=StringType)
Yahtzee_Turn1.attributes={Yahtzee_Turn1_Dice}

# Yahtzee_Scoring1 class attributes and methods
Yahtzee_Scoring1_Temp: Property = Property(name="Temp", type=StringType)
Yahtzee_Scoring1.attributes={Yahtzee_Scoring1_Temp}

# Yahtzee_Players1 class attributes and methods
Yahtzee_Players1_compScore: Property = Property(name="compScore", type=StringType)
Yahtzee_Players1_playerScore: Property = Property(name="playerScore", type=StringType)
Yahtzee_Players1.attributes={Yahtzee_Players1_playerScore, Yahtzee_Players1_compScore}

# Display class attributes and methods

# Get_Player_Name_external class attributes and methods

# Get_Instructions_external class attributes and methods

# Roll_First_external class attributes and methods

# Game_Start_external class attributes and methods

# Computer_Turn_external class attributes and methods

# Roll_Dice_external class attributes and methods

# Score_Roll_external class attributes and methods

# Next_Turn_external class attributes and methods

# Announce_Winner_external class attributes and methods

# Play_Again_external class attributes and methods

# Relationships
Scoring_Turn: BinaryAssociation = BinaryAssociation(
    name="Scoring_Turn",
    ends={
        Property(name="turn0", type=Yahtzee_Turn, multiplicity=Multiplicity(0, 1)),
        Property(name="scoring1", type=Yahtzee_Scoring, multiplicity=Multiplicity(0, 1))
    }
)
Turn_Game: BinaryAssociation = BinaryAssociation(
    name="Turn_Game",
    ends={
        Property(name="game2", type=Yahtzee_Game, multiplicity=Multiplicity(0, 1)),
        Property(name="turn3", type=Yahtzee_Turn, multiplicity=Multiplicity(0, 1))
    }
)
Turn_Players: BinaryAssociation = BinaryAssociation(
    name="Turn_Players",
    ends={
        Property(name="players4", type=Yahtzee_Players, multiplicity=Multiplicity(0, 1)),
        Property(name="turn5", type=Yahtzee_Turn, multiplicity=Multiplicity(0, 1))
    }
)
Game_Players: BinaryAssociation = BinaryAssociation(
    name="Game_Players",
    ends={
        Property(name="players6", type=Yahtzee_Players, multiplicity=Multiplicity(0, 1)),
        Property(name="game7", type=Yahtzee_Game, multiplicity=Multiplicity(0, 1))
    }
)
Scoring_Players: BinaryAssociation = BinaryAssociation(
    name="Scoring_Players",
    ends={
        Property(name="players8", type=Yahtzee_Players, multiplicity=Multiplicity(0, 1)),
        Property(name="scoring9", type=Yahtzee_Scoring, multiplicity=Multiplicity(0, 1))
    }
)
Turn_Scoring: BinaryAssociation = BinaryAssociation(
    name="Turn_Scoring",
    ends={
        Property(name="scoring10", type=Scoring, multiplicity=Multiplicity(0, 1)),
        Property(name="turn11", type=Turn, multiplicity=Multiplicity(0, 1))
    }
)
Scoring_Players1: BinaryAssociation = BinaryAssociation(
    name="Scoring_Players1",
    ends={
        Property(name="players12", type=Players, multiplicity=Multiplicity(0, 1)),
        Property(name="scoring13", type=Scoring, multiplicity=Multiplicity(0, 1))
    }
)
Get_Instructions_Get_Player_Name: BinaryAssociation = BinaryAssociation(
    name="Get_Instructions_Get_Player_Name",
    ends={
        Property(name="get_Player_Name14", type=Get_Player_Name_external, multiplicity=Multiplicity(0, 1)),
        Property(name="get_Instructions15", type=Get_Instructions_external, multiplicity=Multiplicity(0, 1))
    }
)
Get_Player_Name_Roll_First: BinaryAssociation = BinaryAssociation(
    name="Get_Player_Name_Roll_First",
    ends={
        Property(name="roll_First16", type=Roll_First_external, multiplicity=Multiplicity(0, 1)),
        Property(name="get_Player_Name17", type=Get_Player_Name_external, multiplicity=Multiplicity(0, 1))
    }
)
Roll_First_Game_Start: BinaryAssociation = BinaryAssociation(
    name="Roll_First_Game_Start",
    ends={
        Property(name="game_Start18", type=Game_Start_external, multiplicity=Multiplicity(0, 1)),
        Property(name="roll_First19", type=Roll_First_external, multiplicity=Multiplicity(0, 1))
    }
)
Game_Start_Computer_Turn: BinaryAssociation = BinaryAssociation(
    name="Game_Start_Computer_Turn",
    ends={
        Property(name="computer_Turn20", type=Computer_Turn_external, multiplicity=Multiplicity(0, 1)),
        Property(name="game_Start21", type=Game_Start_external, multiplicity=Multiplicity(0, 1))
    }
)
Game_Start_UseCase: BinaryAssociation = BinaryAssociation(
    name="Game_Start_UseCase",
    ends={
        Property(name="useCase22", type=Roll_Dice_external, multiplicity=Multiplicity(0, 1)),
        Property(name="game_Start23", type=Game_Start_external, multiplicity=Multiplicity(0, 1))
    }
)
Roll_Dice_Score_Roll: BinaryAssociation = BinaryAssociation(
    name="Roll_Dice_Score_Roll",
    ends={
        Property(name="score_Roll24", type=Score_Roll_external, multiplicity=Multiplicity(0, 1)),
        Property(name="roll_Dice25", type=Roll_Dice_external, multiplicity=Multiplicity(0, 1))
    }
)
Computer_Turn_Next_Turn: BinaryAssociation = BinaryAssociation(
    name="Computer_Turn_Next_Turn",
    ends={
        Property(name="next_Turn26", type=Next_Turn_external, multiplicity=Multiplicity(0, 1)),
        Property(name="computer_Turn27", type=Computer_Turn_external, multiplicity=Multiplicity(0, 1))
    }
)
Roll_Dice_Next_Turn: BinaryAssociation = BinaryAssociation(
    name="Roll_Dice_Next_Turn",
    ends={
        Property(name="next_Turn28", type=Next_Turn_external, multiplicity=Multiplicity(0, 1)),
        Property(name="roll_Dice29", type=Roll_Dice_external, multiplicity=Multiplicity(0, 1))
    }
)
Next_Turn_Announce_Winner: BinaryAssociation = BinaryAssociation(
    name="Next_Turn_Announce_Winner",
    ends={
        Property(name="announce_Winner30", type=Announce_Winner_external, multiplicity=Multiplicity(0, 1)),
        Property(name="next_Turn31", type=Next_Turn_external, multiplicity=Multiplicity(0, 1))
    }
)
Announce_Winner_Play_Again: BinaryAssociation = BinaryAssociation(
    name="Announce_Winner_Play_Again",
    ends={
        Property(name="play_Again32", type=Play_Again_external, multiplicity=Multiplicity(0, 1)),
        Property(name="announce_Winner33", type=Announce_Winner_external, multiplicity=Multiplicity(0, 1))
    }
)
Roll_First_Play_Again: BinaryAssociation = BinaryAssociation(
    name="Roll_First_Play_Again",
    ends={
        Property(name="play_Again34", type=Play_Again_external, multiplicity=Multiplicity(0, 1)),
        Property(name="roll_First35", type=Roll_First_external, multiplicity=Multiplicity(0, 1))
    }
)
Player_Get_Instructions: BinaryAssociation = BinaryAssociation(
    name="Player_Get_Instructions",
    ends={
        Property(name="get_Instructions36", type=Get_Instructions_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player37", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Get_Player_Name: BinaryAssociation = BinaryAssociation(
    name="Player_Get_Player_Name",
    ends={
        Property(name="get_Player_Name38", type=Get_Player_Name_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player39", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Roll_First: BinaryAssociation = BinaryAssociation(
    name="Player_Roll_First",
    ends={
        Property(name="roll_First40", type=Roll_First_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player41", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Game_Start: BinaryAssociation = BinaryAssociation(
    name="Player_Game_Start",
    ends={
        Property(name="game_Start42", type=Game_Start_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player43", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Roll_Dice: BinaryAssociation = BinaryAssociation(
    name="Player_Roll_Dice",
    ends={
        Property(name="roll_Dice44", type=Roll_Dice_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player45", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Display_Players: BinaryAssociation = BinaryAssociation(
    name="Display_Players",
    ends={
        Property(name="players50", type=Yahtzee_Players1, multiplicity=Multiplicity(0, 1)),
        Property(name="display51", type=Yahtzee_Display1, multiplicity=Multiplicity(0, 1))
    }
)
Display_Turn: BinaryAssociation = BinaryAssociation(
    name="Display_Turn",
    ends={
        Property(name="turn52", type=Yahtzee_Turn1, multiplicity=Multiplicity(0, 1)),
        Property(name="display53", type=Yahtzee_Display1, multiplicity=Multiplicity(0, 1))
    }
)
Display_Scoring: BinaryAssociation = BinaryAssociation(
    name="Display_Scoring",
    ends={
        Property(name="scoring54", type=Yahtzee_Scoring1, multiplicity=Multiplicity(0, 1)),
        Property(name="display55", type=Yahtzee_Display1, multiplicity=Multiplicity(0, 1))
    }
)
Scoring_Turn1: BinaryAssociation = BinaryAssociation(
    name="Scoring_Turn1",
    ends={
        Property(name="turn56", type=Yahtzee_Turn1, multiplicity=Multiplicity(0, 1)),
        Property(name="scoring57", type=Yahtzee_Scoring1, multiplicity=Multiplicity(0, 1))
    }
)
Scoring_Display: BinaryAssociation = BinaryAssociation(
    name="Scoring_Display",
    ends={
        Property(name="display58", type=Display, multiplicity=Multiplicity(0, 1)),
        Property(name="scoring59", type=Scoring, multiplicity=Multiplicity(0, 1))
    }
)
Player_Play_Again: BinaryAssociation = BinaryAssociation(
    name="Player_Play_Again",
    ends={
        Property(name="play_Again46", type=Play_Again_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player47", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Score_Roll: BinaryAssociation = BinaryAssociation(
    name="Player_Score_Roll",
    ends={
        Property(name="score_Roll48", type=Score_Roll_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player49", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4f81af06_c9fe_4739_96e7_53591bd36950",
    types={Yahtzee_Game, Yahtzee_Turn, Yahtzee_Scoring, Yahtzee_Display, Yahtzee_Players, Class_, Class1, Scoring, Turn, Players, Yahtzee_Component, Player_Actor, Yahtzee_Display1, Yahtzee_Turn1, Yahtzee_Scoring1, Yahtzee_Players1, Display, Get_Player_Name_external, Get_Instructions_external, Roll_First_external, Game_Start_external, Computer_Turn_external, Roll_Dice_external, Score_Roll_external, Next_Turn_external, Announce_Winner_external, Play_Again_external},
    associations={Scoring_Turn, Turn_Game, Turn_Players, Game_Players, Scoring_Players, Turn_Scoring, Scoring_Players1, Get_Instructions_Get_Player_Name, Get_Player_Name_Roll_First, Roll_First_Game_Start, Game_Start_Computer_Turn, Game_Start_UseCase, Roll_Dice_Score_Roll, Computer_Turn_Next_Turn, Roll_Dice_Next_Turn, Next_Turn_Announce_Winner, Announce_Winner_Play_Again, Roll_First_Play_Again, Player_Get_Instructions, Player_Get_Player_Name, Player_Roll_First, Player_Game_Start, Player_Roll_Dice, Display_Players, Display_Turn, Display_Scoring, Scoring_Turn1, Scoring_Display, Player_Play_Again, Player_Score_Roll},
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