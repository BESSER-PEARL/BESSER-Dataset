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
Property_: Enumeration = Enumeration(
    name="Property",
    literals={
            
    }
)

# Classes
Player = Class(name="Player")
Class_ = Class(name="Class")
Random = Class(name="Random")
Board = Class(name="Board")
Money = Class(name="Money")
Board1 = Class(name="Board1")
Dice = Class(name="Dice")
AIPlayer = Class(name="AIPlayer")
Jail = Class(name="Jail")
Chance = Class(name="Chance")
BoardGUI = Class(name="BoardGUI")
JFrame = Class(name="JFrame")
PlayerIcon = Class(name="PlayerIcon")
IncomeTax = Class(name="IncomeTax")
FreeParking = Class(name="FreeParking")

# Player class attributes and methods
Player_isRetire: Property = Property(name="isRetire", type=BooleanType)
Player_isAI: Property = Property(name="isAI", type=BooleanType)
Player_isBankrupt: Property = Property(name="isBankrupt", type=BooleanType)
Player_board: Property = Property(name="board", type=Board)
Player_rand: Property = Property(name="rand", type=Random)
Player_INITIAL_MONEY: Property = Property(name="INITIAL_MONEY", type=IntegerType)
Player_INITIAL_POSITION: Property = Property(name="INITIAL_POSITION", type=IntegerType)
Player_PASS_GO_MONEY: Property = Property(name="PASS_GO_MONEY", type=IntegerType)
Player_name: Property = Property(name="name", type=StringType)
Player_money: Property = Property(name="money", type=Money)
Player_position: Property = Property(name="position", type=IntegerType)
Player_property: Property = Property(name="property", type=Property_)
Player_inJail: Property = Property(name="inJail", type=BooleanType)
Player.attributes={Player_isRetire, Player_money, Player_name, Player_property, Player_isBankrupt, Player_rand, Player_position, Player_PASS_GO_MONEY, Player_board, Player_isAI, Player_INITIAL_POSITION, Player_INITIAL_MONEY, Player_inJail}

# Class class attributes and methods

# Random class attributes and methods

# Board class attributes and methods

# Money class attributes and methods
Money_money: Property = Property(name="money", type=IntegerType)
Money.attributes={Money_money}

# Board1 class attributes and methods
Board1_boardSize: Property = Property(name="boardSize", type=IntegerType)
Board1.attributes={Board1_boardSize}

# Dice class attributes and methods
Dice_firstValue: Property = Property(name="firstValue", type=IntegerType)
Dice_secondValue: Property = Property(name="secondValue", type=IntegerType)
Dice_randomNumber: Property = Property(name="randomNumber", type=Random)
Dice.attributes={Dice_firstValue, Dice_secondValue, Dice_randomNumber}

# AIPlayer class attributes and methods

# Jail class attributes and methods
Jail_JailPosition: Property = Property(name="JailPosition", type=IntegerType)
Jail_jailFine: Property = Property(name="jailFine", type=IntegerType)
Jail.attributes={Jail_JailPosition, Jail_jailFine}

# Chance class attributes and methods
Chance_amount: Property = Property(name="amount", type=Random)
Chance.attributes={Chance_amount}

# BoardGUI class attributes and methods
BoardGUI_frame: Property = Property(name="frame", type=JFrame)
BoardGUI.attributes={BoardGUI_frame}

# JFrame class attributes and methods

# PlayerIcon class attributes and methods
PlayerIcon_icon: Property = Property(name="icon", type=StringType)
PlayerIcon.attributes={PlayerIcon_icon}

# IncomeTax class attributes and methods
IncomeTax_taxRate: Property = Property(name="taxRate", type=FloatType)
IncomeTax.attributes={IncomeTax_taxRate}

# FreeParking class attributes and methods

# Relationships
Money_Player: BinaryAssociation = BinaryAssociation(
    name="Money_Player",
    ends={
        Property(name="player0", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="money1", type=Money, multiplicity=Multiplicity(1, 1))
    }
)
Board_Player: BinaryAssociation = BinaryAssociation(
    name="Board_Player",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(0, 9999)),
        Property(name="board3", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
PlayerIcon_BoardGUI: BinaryAssociation = BinaryAssociation(
    name="PlayerIcon_BoardGUI",
    ends={
        Property(name="boardGUI4", type=BoardGUI, multiplicity=Multiplicity(1, 1)),
        Property(name="playerIcon5", type=PlayerIcon, multiplicity=Multiplicity(0, 9999))
    }
)
Board_FreeParking: BinaryAssociation = BinaryAssociation(
    name="Board_FreeParking",
    ends={
        Property(name="freeParking6", type=FreeParking, multiplicity=Multiplicity(1, 1)),
        Property(name="board7", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
Board_IncomeTax: BinaryAssociation = BinaryAssociation(
    name="Board_IncomeTax",
    ends={
        Property(name="incomeTax8", type=IncomeTax, multiplicity=Multiplicity(1, 1)),
        Property(name="board9", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
Board_Dice: BinaryAssociation = BinaryAssociation(
    name="Board_Dice",
    ends={
        Property(name="dice10", type=Dice, multiplicity=Multiplicity(1, 1)),
        Property(name="board11", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
Board_Jail: BinaryAssociation = BinaryAssociation(
    name="Board_Jail",
    ends={
        Property(name="jail12", type=Jail, multiplicity=Multiplicity(1, 1)),
        Property(name="board13", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
Board_Chance: BinaryAssociation = BinaryAssociation(
    name="Board_Chance",
    ends={
        Property(name="chance14", type=Chance, multiplicity=Multiplicity(0, 9999)),
        Property(name="board15", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
BoardGUI_Board: BinaryAssociation = BinaryAssociation(
    name="BoardGUI_Board",
    ends={
        Property(name="board16", type=Board1, multiplicity=Multiplicity(1, 1)),
        Property(name="boardGUI17", type=BoardGUI, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c58bd0b8_1bbc_4039_ba31_a39e964319d6",
    types={Player, Class_, Random, Board, Money, Board1, Dice, AIPlayer, Jail, Chance, BoardGUI, JFrame, PlayerIcon, IncomeTax, FreeParking, Property_},
    associations={Money_Player, Board_Player, PlayerIcon_BoardGUI, Board_FreeParking, Board_IncomeTax, Board_Dice, Board_Jail, Board_Chance, BoardGUI_Board},
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