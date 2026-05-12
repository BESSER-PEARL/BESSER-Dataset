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
FreeParking = Class(name="FreeParking")

# Player class attributes and methods
Player_board: Property = Property(name="board", type=Board)
Player_rand: Property = Property(name="rand", type=Random)
Player_INITIAL_MONEY: Property = Property(name="INITIAL_MONEY", type=IntegerType)
Player_INITIAL_POSITION: Property = Property(name="INITIAL_POSITION", type=IntegerType)
Player_PASS_GO_MONEY: Property = Property(name="PASS_GO_MONEY", type=IntegerType)
Player_name: Property = Property(name="name", type=StringType)
Player_money: Property = Property(name="money", type=Money)
Player_position: Property = Property(name="position", type=IntegerType)
Player_property: Property = Property(name="property", type=StringType)
Player_isRetire: Property = Property(name="isRetire", type=BooleanType)
Player_isAI: Property = Property(name="isAI", type=BooleanType)
Player_isBankrupt: Property = Property(name="isBankrupt", type=BooleanType)
Player.attributes={Player_board, Player_PASS_GO_MONEY, Player_isRetire, Player_property, Player_isAI, Player_INITIAL_POSITION, Player_isBankrupt, Player_name, Player_INITIAL_MONEY, Player_rand, Player_position, Player_money}

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
Dice.attributes={Dice_randomNumber, Dice_firstValue, Dice_secondValue}

# AIPlayer class attributes and methods

# FreeParking class attributes and methods

# Relationships
Board_FreeParking: BinaryAssociation = BinaryAssociation(
    name="Board_FreeParking",
    ends={
        Property(name="freeParking4", type=FreeParking, multiplicity=Multiplicity(1, 1)),
        Property(name="board5", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
Board_Dice: BinaryAssociation = BinaryAssociation(
    name="Board_Dice",
    ends={
        Property(name="dice6", type=Dice, multiplicity=Multiplicity(1, 1)),
        Property(name="board7", type=Board1, multiplicity=Multiplicity(1, 1))
    }
)
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

# Domain Model
domain_model = DomainModel(
    name="b0b03da3_3208_4747_bed7_f0ef9c111bb0",
    types={Player, Class_, Random, Board, Money, Board1, Dice, AIPlayer, FreeParking, Property_},
    associations={Board_FreeParking, Board_Dice, Money_Player, Board_Player},
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